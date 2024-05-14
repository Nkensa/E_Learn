from django.urls import path
from E_LearnSite.views import *

urlpatterns = [
    path('', index, name='index')
]
