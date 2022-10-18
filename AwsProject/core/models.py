from django.db import models


class StatusChoices(models.IntegerChoices):
    FAZER = 1, 'A Fazer'
    FAZENDO = 2, 'Fazendo'
    FEITO = 3, 'Feito'


class TarefaModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=StatusChoices.choices)

    def __str__(self):
        return f'{self.name} - {self.description}'
