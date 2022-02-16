# Generated by Django 3.2 on 2021-06-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0005_auto_20210616_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='locality',
            name='childs',
            field=models.ManyToManyField(related_name='children', through='roads.Family', to='roads.Locality'),
        ),
    ]
