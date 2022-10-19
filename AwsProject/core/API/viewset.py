import objects as objects
from rest_framework import viewsets

from AwsProject.core.API.serializers import TarefaSerializer, MultipleSerializerModelViewSet, TarefaCreateSerializer
from AwsProject.core.models import TarefaModel


class TarefaViwSet(MultipleSerializerModelViewSet):
    serializer_class = TarefaSerializer
    create_serializer_class = TarefaCreateSerializer
    queryset = TarefaModel.objects.all()



