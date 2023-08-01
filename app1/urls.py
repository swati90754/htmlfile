from django.urls import path
from .views import *
urlpatterns = [
    path('sv/', student_view, name='student_url'),
    path('dv/', display_view, name='display_url'),
    path('dev/<int:pk>/', delete_view, name='delete_url'),
    path('uv/<int:pk>/', update_view, name='update_url'),
   
]