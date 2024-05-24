from django.db import models

from Account.models import CustomUser
from E_LearnApp_Admin.models import Classroom, Subject


# Create your models here.

class Adventure(models.Model):
    adventure_id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.classroom} - {', '.join([subject.name_subject for subject in self.subjects.all()])}"
