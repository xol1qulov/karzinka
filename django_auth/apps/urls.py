import profile

from django.contrib import admin
from django.urls import path

from apps.views import sign_up, sign_in, users_list, user_profile, my_profile, chat

urlpatterns = [
    path('', users_list, name='users-list'),
    path('sign-up', sign_up, name='sign-up'),
    path('sign-in', sign_in, name='sign-in'),
    path('user-profile/<int:pk>', user_profile, name='user-profile'),
    path('chat/<int:user_id>', chat, name='user-chat'),
    path('my-profile', my_profile, name='my-profile')
]
