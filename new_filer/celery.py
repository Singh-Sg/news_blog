
import os
from celery import Celery




os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_filer.settings")
app = Celery("new_filer")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
