"""
WSGI config for doctor_appointmen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# 👇 इथे तुझ्या project folder चं नाव द्यायचं
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doctor_appointmen.settings")

application = get_wsgi_application()
