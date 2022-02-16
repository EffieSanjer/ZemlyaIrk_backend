# Generated by Django 3.2 on 2021-06-10 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0016_auto_20210608_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='test',
        ),
        migrations.AlterField(
            model_name='members',
            name='date_add',
            field=models.DateField(default=datetime.date(2021, 6, 10), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_start',
            field=models.DateField(default=datetime.date(2021, 6, 10), verbose_name='Дата начала'),
        ),
    ]
