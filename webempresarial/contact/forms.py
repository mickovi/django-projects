from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), max_length=50)
    email = forms.EmailField(label='Correo electrónico', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu correo'}
    ), max_length=50)
    content = forms.CharField(label='Consulta', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu consulta'}
    ), min_length=10, max_length=200)