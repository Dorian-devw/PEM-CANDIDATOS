from django.db import models

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    partido = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    fotoUrl = models.URLField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    fechaNacimiento = models.DateField(blank=True, null=True)
    profesion = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

class Proyecto(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name="proyectos")
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    urlFuente = models.URLField()

class Denuncia(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name="denuncias")
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    urlFuente = models.URLField()