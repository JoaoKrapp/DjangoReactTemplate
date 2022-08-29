from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('feed/', index),
    path('login/', index),
]
