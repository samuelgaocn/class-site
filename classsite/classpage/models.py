from django.db import models

# Create your models here.
class News(models.Model):
    titlemax = models.CharField(max_length = 30)
    titlemin = models.CharField(max_length = 40)
    introduction = models.CharField(max_length = 150)
    time = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    photot = models.ImageField()

class Announcement(models.Model):
    title = models.CharField(max_length = 30)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    Author = models.CharField(max_length = 20)

    
class File_math(models.Model):
    name = models.CharField(max_length = 30)
    file_ppt = models.FileField()
    time = models.DateTimeField(auto_now_add = True)
    people = models.CharField(max_length = 30)


class File_language(models.Model):
    name = models.CharField(max_length = 30)
    file_ppt = models.FileField()
    time = models.DateTimeField(auto_now_add = True)
    people = models.CharField(max_length = 30)


class File_others(models.Model):
    name = models.CharField(max_length = 30)
    file_ppt = models.FileField()
    time = models.DateTimeField(auto_now_add = True)
    people = models.CharField(max_length = 30)


