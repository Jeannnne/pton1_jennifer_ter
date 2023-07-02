import random
import string

from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Collaborator


def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


class APIKeysView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="GET /api/api-keys/ Permet d'obtenir la clé API d'un "
                                               "utilisateur, il doit se login dans le body.")
    def get(self, request):
        user = Collaborator.objects.get(id=request.user.id)
        if user:
            return Response(data={"api_key": user.api_key}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="POST /api/api-keys/ Permet de générer une nouvelle clé "
                                               "API et un nouveau secret API, a besoin d'un token.")
    def post(self, request):
        user = Collaborator.objects.get(id=request.user.id)

        if user:
            api_key = generate_random_string(64)
            api_secret = generate_random_string(64)
            user.api_key = api_key
            user.api_secret = make_password(api_secret)
            user.save()
            return Response(data={"api_key": api_key, "api_secret": api_secret}, status=status.HTTP_200_OK)


# New
class ValidateAPIKeysView(APIView):
    @swagger_auto_schema(operation_description="POST /api/validate-api-keys/ "
                                               "Permet de valider une clé API et un "
                                               "secret API.")
    def get(self, request):
        api_key = request.headers.get("api-key")
        api_secret = request.headers.get("api-secret")

        try:
            user = Collaborator.objects.get(api_key=api_key)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user:
            if user.api_key == api_key and user.has_valid_api_secret(api_secret):
                return Response(data={"valid": True}, status=status.HTTP_200_OK)
            return Response(data={"valid": False}, status=status.HTTP_200_OK)


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
