from rest_framework import viewsets

from AwsProject.accounts.API.serializers import MemberSerializer
from AwsProject.accounts.models import Member


class MemberViewset(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all().exclude(is_staff=True)