from django.db import models
from cliente.models import Cliente

class Transferencia(models.Model):
    quantia = models.FloatField()
    destinatario_cpf = models.CharField(max_length=11)
    data_dep = models.DateField()
    comentario = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
