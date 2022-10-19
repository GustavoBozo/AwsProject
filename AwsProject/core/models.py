from django.db import models


class BetterIntegerChoices(models.IntegerChoices):
    @classmethod
    def dict(cls):
        return [{item[0]: item[1]} for item in cls.choices]

    @classmethod
    def getValue(cls, label):
        try:
            labels = [lbl.lower() for lbl in cls.labels]
            pos = labels.index(label.lower())
            return cls.values[pos]
        except ValueError:
            return None

    @classmethod
    def getLabel(cls, value):
        try:
            pos = cls.values.index(value)
            return cls.labels[pos]
        except ValueError:
            return None


class StatusChoices(BetterIntegerChoices):
    FAZER = 1, 'A Fazer'
    FAZENDO = 2, 'Fazendo'
    FEITO = 3, 'Feito'


class TarefaModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=StatusChoices.choices)

    def __str__(self):
        return f'{self.name} - {self.description}'

    @property
    def getStatus(self):
        return StatusChoices.getLabel(self.status)