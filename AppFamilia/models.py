from django.db import models

class Familiar(models.Model):

    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    numeroCelular = models.IntegerField()
    fechaNacimiento = models.DateField()