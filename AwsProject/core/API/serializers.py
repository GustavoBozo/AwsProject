from rest_framework import serializers

from AwsProject.core.models import TarefaModel


class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TarefaModel
        fields = '__all__'

