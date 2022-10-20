"""
ASGI config for home project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from decouple import config
from django.core.asgi import get_asgi_application

environment = config('ENVIRONMENT')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'home.settings.{environment}')

application = get_asgi_application()
