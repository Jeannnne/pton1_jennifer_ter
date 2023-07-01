from dj_rest_auth.views import LoginView, LogoutView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.utils import APIKeysView, ValidateAPIKeysView
from api.views import CollaboratorViewSet

router = DefaultRouter()
router.register('collaborators', CollaboratorViewSet, basename='collaborators')

urlpatterns = [
    path('', include(router.urls)),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api-keys/', APIKeysView.as_view(), name='api-keys'),
    path('validate-api-keys/', ValidateAPIKeysView.as_view(), name='validate-api-keys')
]
