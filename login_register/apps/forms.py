from django import forms
from apps.models import User


class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'username', 'email', 'password', 'first_name', 'last_name'


class UsersFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = 'username', 'email', 'password', 'image', 'website', 'street', \
            'city', 'state', 'phone',  'job', 'hobbies', 'first_name', 'last_name'
