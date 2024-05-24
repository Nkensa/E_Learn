from django.urls import path
from E_Learniverse.views import *

urlpatterns = [
    path('welcome_app/', welcomeApp, name='welcome_app'),
    path('my_adventure/', my_adventure, name='my_adventure'),
    path('profil_user/<int:pk>', profil_user, name='profil'),
    # path('profil/', profil, name='profil'),
]
