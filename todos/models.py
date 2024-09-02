from django.db import models


class Todo(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data_criacao = models.DateField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateField(null=False, blank=False)
    data_finalizacao = models.DateField(null=True)
