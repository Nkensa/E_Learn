from django.urls import path

from Account.views import *

urlpatterns = [
    path('sign_up/', sign_up, name='register'),
    path('sign_in/', user_login, name='login'),
]