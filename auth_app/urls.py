from django.urls import path
from .views import *
urlpatterns = [
    path('rv/', register_view, name='register_url'),
    path('in/', login_view, name='login_url'),
    path('ot/', logout_view, name='logout_url')

]