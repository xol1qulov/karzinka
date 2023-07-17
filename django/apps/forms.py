from django import forms
from apps.models import Contact


class UsersForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
