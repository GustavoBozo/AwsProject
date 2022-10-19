from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from AwsProject.core.models import TarefaModel


class Member(AbstractUser):
    tarefa = models.ForeignKey('core.TarefaModel', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username



