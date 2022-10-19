from rest_framework import serializers

from AwsProject.accounts.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'username', 'tarefa']
