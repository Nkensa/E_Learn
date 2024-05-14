from django.urls import path
from django.views.generic import DetailView

from E_LearnApp_Admin.views import *

urlpatterns = [
    path('Home_Admin', WelcomeAdmin, name='home_admin'),
    path('Liste_Users', Users_list, name='myusers'),
    path('Liste_Users/create/', create_user, name='create_user'),
    path('Liste_Users/<int:pk>', detail_user, name='detail_user'),
    path('Liste_Users/<int:pk>/update', update_user, name='updateuser'),
    path('Subjects', subjects, name='subjects'),
    path('Classrooms', classrooms, name='classrooms'),
    path('Classrooms/<int:classroom_id>', edit_classroom, name='edit_classroom'),

]

