from django.urls import path
from news.views import trigger_celery_task

urlpatterns = [
    path('trigger-task/', trigger_celery_task, name='trigger-celery-task'),
]
