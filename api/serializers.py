from rest_framework import serializers

from users.models import Collaborator, Service


class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collaborator
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'date_left', 'service', 'current_job',
                  'profile_picture', 'company_date_joined', 'service', 'current_job', 'company_date_joined']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['parent_group', 'name']
