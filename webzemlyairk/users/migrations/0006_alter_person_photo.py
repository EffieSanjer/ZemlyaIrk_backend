# Generated by Django 3.2 on 2021-06-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_person_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото'),
        ),
    ]
