# Generated by Django 3.2 on 2021-06-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='role_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Роль'),
        ),
    ]
