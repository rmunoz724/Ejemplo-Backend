from django.db import models
from django.utils import timezone

class Persona(models.Model):
    rut = models.CharField(max_length=13,primary_key=True)
    nombre = models.CharField(max_length=15, null=False)
    apellidos = models.CharField(max_length=20, null=False)
    direccion = models.CharField(max_length=50, null=False)
    correo_electronico = models.EmailField(max_length=70, null=False)
    fecha_nacimiento = models.DateField(default= timezone.localdate)


