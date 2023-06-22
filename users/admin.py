from django.contrib import admin

from users.models import Collaborator, Service


# Register your models here.

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    exclude = ['password', 'last_login']
    list_display = ['username', 'email', 'current_job', 'date_joined', 'date_left']
    list_filter = ['date_joined', 'date_left']
    search_fields = ['username', 'email', 'current_job']
    readonly_fields = ['date_joined']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_group']
    list_filter = ['parent_group']
    search_fields = ['name']
