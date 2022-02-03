from django.db import models
from cliente.models import Cliente

class Deposito(models.Model):
    quantia = models.FloatField()
    destinatario_cpf = models.CharField(max_length=11)
    data_dep = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
