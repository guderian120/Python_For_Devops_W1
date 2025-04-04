
from django.urls import path
from .views import *


urlpatterns = [
            path("metrics/", get_metrics, name='get_metrics'),       
            path("dashboard/", display_dashboard, name='display_dashboard'), 
]
