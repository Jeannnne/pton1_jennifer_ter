from dj_rest_auth.views import LoginView, LogoutView
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from api.utils import APIKeysView, ValidateAPIKeysView
from api.views import CollaboratorViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'collaborators', CollaboratorViewSet, basename='collaborator')
router.register(r'services', ServiceViewSet, basename='service')

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API Documentation for PTON1",
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),

    path('api-docs/', schema_view.with_ui('redoc'), name='api-docs'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api-keys/', APIKeysView.as_view(), name='api-keys'),
    path('validate-api-keys/', ValidateAPIKeysView.as_view(), name='validate-api-keys')
]
