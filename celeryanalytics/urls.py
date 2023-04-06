from django.urls import path, re_path

from . import views
from .api import api

app_name = 'celery'

urlpatterns = [
    path('queue/', views.react_main, name='celery_mon'),
    re_path(r'^api/', api.urls),

]
