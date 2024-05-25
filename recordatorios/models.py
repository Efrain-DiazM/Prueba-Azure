from django.db import models

class Recordatorio(models.Model):
    nombre_medicamento = models.CharField(max_length=200)
    hora_alerta = models.TimeField()
    comentario = models.TextField()

    def __str__(self):
        return self.nombre_medicamento
