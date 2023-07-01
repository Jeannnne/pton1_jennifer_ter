from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import CollaboratorSerializer, ServiceSerializer
from users.models import Collaborator, Service


# Create your views here.
@swagger_auto_schema(
        operation_description="CRUD for a Collaborator"
    )
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Get a list of all collaborators"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Get a collaborator by id"
))
class CollaboratorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


@swagger_auto_schema(
        operation_description="CRUD for a Service"
    )
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Get a list of all services"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Get a service by id"
))
class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

