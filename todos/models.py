from django.db import models
from datetime import date

class Todo(models.Model):
    titulo = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False)
    data_criacao = models.DateField(
        verbose_name="Criado em", auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateField(
        verbose_name="Data de Entrega", null=False, blank=False)
    data_finalizacao = models.DateField(
        verbose_name="Finalizado em", null=True)
    class Meta:
        ordering = ["data_entrega"]

    def mark_has_complete(self):
        if not self.data_finalizacao:
            self.data_finalizacao = date.today()
            self.save()