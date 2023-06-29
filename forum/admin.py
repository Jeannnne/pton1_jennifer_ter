from django.contrib import admin

from forum.models import *


# Register your models here.

@admin.register(Subject)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_open', 'author', 'created_at']
    date_hierarchy = "created_at"


@admin.register(CustomMessage)
class CustomMessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_at', 'author']
    date_hierarchy = "created_at"
