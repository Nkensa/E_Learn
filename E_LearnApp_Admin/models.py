from django.db import models
from Account.models import CustomUser

# Create your models here.

class Subject(models.Model):
    id_subject = models.AutoField(primary_key=True)
    name_subject = models.CharField(max_length=255)
    description_subject = models.CharField(max_length=255, null=True)
    photo_subject = models.ImageField(upload_to='Images/images_subjects', height_field=None, width_field=None, default=True, max_length=None, null=True)


    def __str__(self):
        return self.name_subject


class Classroom(models.Model):
    id_classroom = models.AutoField(primary_key=True)
    name_classroom = models.CharField(max_length=255)
    custom_user = models.ManyToManyField(CustomUser)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.name_classroom}'


