# Generated by Django 4.2.3 on 2023-07-11 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_rename_job_image_contact_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='job',
            new_name='image',
        ),
    ]