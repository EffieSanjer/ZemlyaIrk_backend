# Generated by Django 3.2 on 2021-06-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0006_alter_request_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='object_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Объект'),
        ),
    ]
