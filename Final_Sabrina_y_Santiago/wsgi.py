import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final_Sabrina_y_Santiago.settings')

application = get_wsgi_application()
