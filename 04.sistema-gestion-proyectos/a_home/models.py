from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion_corta = models.CharField(max_length=255)
  lider_equipo = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="lider_equipo")
  imagen = models.FileField(upload_to="imagenes")
  url = models.URLField(blank=True, null=True)


class Desarrollador(models.Model):
  pass

class Repositorio(models.Model):
  pass

class Servidor(models.Model):
  pass

class Clave(models.Model):
  pass