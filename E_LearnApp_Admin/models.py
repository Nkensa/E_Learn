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


class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    title_Course = models.CharField(max_length=150)
    description_course = models.CharField(max_length=45, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.title_Course

class Chapter(models.Model):
    id_chapter = models.AutoField(primary_key=True)
    title_chapter = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_chapter


class Modules(models.Model):
    id_module = models.AutoField(primary_key=True)
    title_module = models.CharField(max_length=150)
    chapters = models.ManyToManyField(Chapter)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_module


class Lesson(models.Model):
    id_lesson = models.AutoField(primary_key=True)
    title_lesson = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    file_content = models.FileField(upload_to="Lessons", blank=True, null=True)
    module = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    chapters = models.ForeignKey(Course, on_delete=models.CASCADE)
