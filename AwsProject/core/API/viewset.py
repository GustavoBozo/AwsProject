import objects as objects
from rest_framework import viewsets

from AwsProject.core.API.serializers import TarefaSerializer
from AwsProject.core.models import TarefaModel


class TarefaViwSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    queryset = TarefaModel.objects.all()

