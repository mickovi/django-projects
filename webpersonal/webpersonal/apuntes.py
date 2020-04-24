"""
CREAR UN NUEVO PROYECTO
django-admin startproject mi_proyecto
"""

"""
ARCHIVOS BASE:

manage.py: sirve para configurar y gestionar el proyecto desde la terminal
[Carpeta del Proyecto] : Contiene los scripts base del proyecto que contienen configuración la inicial y de despliege
    __init__.py: Indica que la carpeta es un paquete
    settings.py: Es la configuración del proyecto
    urls.py: Maneja las direcciones de la web
    wsgi.py: Contiene la información para desplejar el proyecto en producción
"""

"""
MODO DEBUG:
Muestra valores, rutas y datos sensibles que se mostrarán cuando la web falle. Solo usarlo en modo de producción
y no de despliegue.
"""

"""
CONCEPTOS CLAVE
makemigrations: Le indica a django que hay un modelo nuevo y cree un fichero de migraciones (similar a hacer un add en git?)
migrate: Se aplica la migración a la BD (similar a hacer un commit en git)
https://docs.djangoproject.com/en/3.0/topics/migrations/
ORM:
Modelos
Proyecto:
Apps:
Tipos de campo: https://docs.djangoproject.com/en/3.0/ref/forms/fields/
"""

"""
APPs: Aplicaciones internas que ejecutan funcionalidades específicas
ejem: admin, auth, contenttypes, sessions, etc. Se encuentran en el archivo settings.py.
Django tiene varias apps genéricas, pero permite crear las nuestras

Un proyecto es un conjunto de apps integradas, pero diferentes apps pueden funcionar en otros proyectos.
Iniciar una app:
python manage.py startapp mi_app

ARCHIVOS
Haciendo python manage.py startapp core creamos una nueva app que genera varios archivos:

[migrations]: Se genera un archivo de migraciones cuando se crean modelos
    __init.py__:
__init.py__:
admin.py:
apps.py:
models.py: Donde se crean los modelos (clases enlazadas a la BD)
tests.py:
views.py: Se definen las vistas de una app (lógica)

"""

"""

"""

"""
TEMPLATE TAG
Sirve para añadir lógica de programación dentro de HTML
block: define un bloque de contenido con un nombre. Ejemplo: {% block un_nombre %}{% endblock %}
url: 
load static:
if:
"""

"""
Pillow: Paquete para manipular diferentes formatos de imágenes
ORM (Obejct Relational Model): Trabajar con objetos mapeados en la BD
"""

"""

"""