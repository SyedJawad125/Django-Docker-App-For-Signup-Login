# # djangoproject/celery.py
# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

# # Create the Celery app
# app = Celery('djangoproject')

# # Load task modules from all registered Django app configs.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Autodiscover tasks from all installed apps.
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')



from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

# Create the Celery app
app = Celery('djangoproject')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from all installed apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
