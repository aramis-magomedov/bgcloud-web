from django.db import models

# Create your models here.
class Boardgame(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=255)
    time_min = models.IntegerField()                  # минимальное время партии 
    time_max = models.IntegerField()                  # максимальное время партии
    age = models.IntegerField()                       # возрастная маркировка
    artist = models.CharField(max_length=64, blank=True)          # дизайнер настольной игры
    designer = models.CharField(max_length=64, blank=True)        # автор настольной игры

class User(models.Model):
    name = models.CharField(max_length=64)
    