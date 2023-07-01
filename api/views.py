from rest_framework import viewsets
from rest_framework_api_key import permissions

from api.serializers import CollaboratorSerializer
from users.models import Collaborator


# Create your views here.
class CollaboratorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.HasAPIKey]
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

