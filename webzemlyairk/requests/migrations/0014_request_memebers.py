# Generated by Django 3.2 on 2021-06-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_person_options'),
        ('requests', '0013_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='memebers',
            field=models.ManyToManyField(through='requests.Members', to='users.Person'),
        ),
    ]
