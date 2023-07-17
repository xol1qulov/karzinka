from django.urls import path

from apps.views import home, create, user, delete_user, home_red

urlpatterns = [
    path('', home, name='home'),
    path('new_home', home_red, name='home_red'),
    path('create/', create, name='create'),
    path('user/<int:pk>/', user, name='user'),
    path('user/<int:pk>/delete/', delete_user, name='delete_user'),
]
