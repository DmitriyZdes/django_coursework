# Generated by Django 5.0.2 on 2024-05-06 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
