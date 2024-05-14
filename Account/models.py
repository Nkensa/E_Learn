from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    id_CustomUser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    pp = models.ImageField(upload_to='Images/users_profil', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.id_CustomUser} - {self.username}'

