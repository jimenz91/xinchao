
from rest_framework.serializers import ModelSerializer
from profiles.models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        exclude = ('id',)
