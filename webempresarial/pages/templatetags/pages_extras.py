from django import template
from pages.models import Pages

# Registrar el template a la librería de templates
register = template.Library()

# Añadimos un decorador que va a implementar una nueva funcionalidad
@register.simple_tag
def get_pages_list():
    pages = Pages.objects.all()
    return pages