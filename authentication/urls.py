from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('demo/', demo, name='demo'),
    path('', views.HelloView.as_view(), name='hello'),
]