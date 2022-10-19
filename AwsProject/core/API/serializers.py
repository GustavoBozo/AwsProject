from rest_framework import serializers, viewsets

from AwsProject.core.models import TarefaModel


class MultipleSerializerModelViewSet(viewsets.ModelViewSet):
    create_serializer_class = None
    retrieve_serializer_class = None
    update_serializer_class = None
    partial_update_serializer_class = None
    destroy_serializer_class = None
    list_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'create':
            return self.getDefaultSerializer(self.create_serializer_class)
        elif self.action == 'retrieve':
            return self.getDefaultSerializer(self.retrieve_serializer_class)
        elif self.action == 'update':
            return self.getDefaultSerializer(self.update_serializer_class)
        elif self.action == 'partial_update':
            return self.getDefaultSerializer(self.partial_update_serializer_class)
        elif self.action == 'destroy':
            return self.getDefaultSerializer(self.destroy_serializer_class)
        elif self.action == 'list':
            return self.getDefaultSerializer(self.list_serializer_class)
        return self.serializer_class

    def getDefaultSerializer(self, serializer_class):
        if serializer_class is not None:
            return serializer_class
        else:
            return self.serializer_class


class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TarefaModel
        fields = ['name', 'description', 'getStatus']


class TarefaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TarefaModel
        fields = '__all__'

