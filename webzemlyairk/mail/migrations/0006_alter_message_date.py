# Generated by Django 3.2 on 2021-06-19 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 19, 17, 52, 4, 506788), verbose_name='Дата'),
        ),
    ]
