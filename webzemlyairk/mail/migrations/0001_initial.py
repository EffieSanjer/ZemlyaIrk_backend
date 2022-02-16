# Generated by Django 3.2 on 2021-06-16 19:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_alter_person_role_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, max_length=250, null=True, verbose_name='Тема')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
                ('date', models.DateField(default=datetime.datetime(2021, 6, 17, 3, 29, 51, 298381), verbose_name='Дата')),
                ('date_marked_sender', models.DateField(verbose_name='Дата отметки отправителем')),
                ('date_marked_receiver', models.DateField(verbose_name='Дата отметки получателем')),
                ('date_sended', models.DateField(verbose_name='Дата отправки')),
                ('date_delete', models.DateField(verbose_name='Дата удаления')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_from', to='users.person')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_to', to='users.person')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
