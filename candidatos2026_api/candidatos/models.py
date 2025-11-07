from django.db import models

class Candidato(models.Model):
    TIPO_CHOICES = [
        ('PRESIDENTE', 'Presidente'),
        ('CONGRESISTA', 'Congresista'),
        ('SENADOR', 'Senador'),
    ]
    nombre = models.CharField(max_length=100)
    partido = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    biografia = models.TextField()
    foto_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"