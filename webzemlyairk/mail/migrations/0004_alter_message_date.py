# Generated by Django 3.2 on 2021-06-17 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 21, 39, 26, 435882), verbose_name='Дата'),
        ),
    ]
