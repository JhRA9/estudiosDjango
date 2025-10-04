from django.db import models

# Create your models here.

# Deben ser clases los modelos

class Carro(models.Model):
    titulo = models.TextField(max_length=250)