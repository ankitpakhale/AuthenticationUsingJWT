from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('demo/', demo, name='demo'),
    path('', views.HelloView.as_view(), name='hello'),
    path('get/', views.Get_data.as_view(), name='get'),
    path('post/', views.Post_data.as_view(), name='post'),

    path('student/', views.Student_data.as_view(), name='student'),
    path('update/', views.Update_data.as_view(), name='update'),
    path('patch/', views.Patch_data.as_view(), name='patch'),
    path('delete/<int:id>', views.Delete_data.as_view(), name='delete'),
]