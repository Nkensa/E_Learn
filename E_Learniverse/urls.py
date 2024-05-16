from django.urls import path
from E_Learniverse.views import *

urlpatterns = [
    path('welcome_app/', welcomeApp, name='welcome_app'),
]
