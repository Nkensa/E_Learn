from django.urls import path
from E_LearnSite.views import *

urlpatterns = [
    path('', index, name='index'),
    path('enregistrer_compte/', sign_up, name='sign_up'),
    path('connexion_compte/', login, name='login'),
]
