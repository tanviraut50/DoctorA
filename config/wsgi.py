import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doctor_appointment.settings")

application = get_wsgi_application()
