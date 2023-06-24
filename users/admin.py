from django.contrib import admin

from users.models import Collaborator, Service


# Register your models here.

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'current_job', 'company_date_joined', 'date_left']
    list_filter = ['date_joined', 'date_left']
    search_fields = ['username', 'email', 'current_job']
    readonly_fields = ['date_joined']
    exclude = ['password', 'last_login', 'groups', 'user_permissions', 'is_active']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_group']
    list_filter = ['parent_group']
    search_fields = ['name']
