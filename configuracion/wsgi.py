"""
Configuracion WSGI para el proyecto BAE Technology.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.configuracion')

application = get_wsgi_application()
