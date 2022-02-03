from django.db import models
from cliente.models import Cliente
from uuid import uuid4

class Transferencia(models.Model):
    id_transf = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quantia = models.FloatField()
    data_transf = models.DateField()
    cliente_cpf_transf = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)

