from django.urls import path, re_path

from . import views

app_name = 'celery'

urlpatterns = [
    #re_path(r'^celery/$', views.celery_admin_view, name='celery_mon'),
]
