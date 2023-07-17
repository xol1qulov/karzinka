from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from apps.models import User, Message


@admin.register(User)
class UserModelAdmin(UserAdmin):
    pass


@admin.register(Message)
class MessageModelAdmin(ModelAdmin):
    list_display = 'id', 'text'
