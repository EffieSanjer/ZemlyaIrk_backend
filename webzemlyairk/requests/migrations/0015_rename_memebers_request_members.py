# Generated by Django 3.2 on 2021-06-06 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0014_request_memebers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='memebers',
            new_name='members',
        ),
    ]
