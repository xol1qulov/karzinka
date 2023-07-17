from django.urls import path

from apps.views import home, register, edit_views

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user/<int:pk>/', edit_views, name='edit_views')
    # path('user/<int:pk>', user_1, name='user_1')
]
