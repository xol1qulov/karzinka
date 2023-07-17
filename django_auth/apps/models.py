from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CharField, ManyToManyField, IntegerField, Model, ForeignKey, CASCADE, \
    DateTimeField, TextField


class User(AbstractUser):
    avatar = ImageField(upload_to='users/', null=True, blank=True)
    website = CharField(max_length=255, null=True, blank=True)
    street = CharField(max_length=255, null=True, blank=True)
    city = CharField(max_length=255, null=True, blank=True)
    state = CharField(max_length=255, null=True, blank=True)
    phone = CharField(max_length=55, null=True, blank=True)

    follow = ManyToManyField('apps.User')
    profile_view = IntegerField(default=0)

    @property
    def avatar_url(self):
        try:
            return self.avatar.url
        except ValueError:
            return 'https://bootdey.com/img/Content/avatar/avatar7.png'


class Message(Model):
    text = TextField()
    author = ForeignKey('apps.User', CASCADE, related_name='my_messages')
    to = ForeignKey('apps.User', CASCADE, related_name='from_messages')
    created_at = DateTimeField(auto_now_add=True)
