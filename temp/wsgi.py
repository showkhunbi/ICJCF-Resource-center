# """
# WSGI config for aces project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aces.settings')

# application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application
import os
import sys

sys.path.append('/opt/bitnami/projects/aces')
os.environ.setdefault("PYTHON_EGG_CACHE",
                      "/opt/bitnami/projects/aces/egg_cache")
os.environ["DJANGO_SETTINGS_MODULE"] = "aces.settings"
application = get_wsgi_application()
