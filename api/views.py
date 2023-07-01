
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import CollaboratorSerializer, ServiceSerializer
from users.models import Collaborator, Service


# Create your views here.
class CollaboratorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

