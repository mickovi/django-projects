from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    # Instaciamos un nuevo formulario vacío
    contact_form = ContactForm()
    # Verificamos que el formulario envia un POST
    if request.method == 'POST':
        # Procesamos el formulario guardando un diccionario data en el objecto contact_form
        contact_form = ContactForm(data=request.POST)
        # Verificamos que todos los campos fueron llenados correctamente
        if contact_form.is_valid():
            # Recuperamos los campos. Si no se escribió nada devolver una cadena vacía
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Si todo es correcto redireccionamos a la misma página (prueba local)
            #return redirect('/contact/?ok') # Mala práctica
            #return redirect(reverse('contact')+'?ok') # Buena práctica

            # Si todo es correcto enviamos un correo (prueba con un servidor de mailtrap.io)
            """email = EmailMessage(
                asunto,
                cuerpo,
                email_origen,
                email_destino, # Lista de todos los correos que queremos enviar el mensaje
                reply_to=[email]
            )"""

            email = EmailMessage(
                'La Caffetiera: Nuevo mensaje',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['moviedor05@gmail.com', 'user1@gmail.com', 'user2@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                # Si todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+'?ok')
            except:
                # Si algo ha fallado, redireccionamos a fail (CODEARLO!)
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})