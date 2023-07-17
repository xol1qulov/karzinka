from django.db import models


class PositionChoices(models.TextChoices):
    JUNIOR = "Junior Developer", 'Junior Developer'
    MIDDLE = "Middle Developer", 'Middle Developer'
    SENIOR = "Senior Developer", 'Senior Developer'


class Contact(models.Model):
    username = models.CharField(max_length=255)
    position = models.CharField(max_length=200, choices=PositionChoices.choices, default=PositionChoices.JUNIOR)
    address = models.CharField(max_length=255, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    job = models.CharField(max_length=20, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-published_at']
        db_table = 'Contact'
