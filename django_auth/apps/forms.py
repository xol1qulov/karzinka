# ModelForm / Form
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from apps.models import User


class UserSignUpModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'username', 'first_name')


class UserChangeProfileModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'state',
                  'city', 'street', 'avatar', 'website')
