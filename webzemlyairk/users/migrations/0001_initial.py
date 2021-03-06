# Generated by Django 3.2.4 on 2021-06-02 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='ФИО')),
                ('phone1', models.CharField(max_length=12, verbose_name='Телефон 1')),
                ('phone2', models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон 2')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('is_client', models.BooleanField(verbose_name='Клиент?')),
                ('position', models.TextField(blank=True, null=True, verbose_name='Должность')),
                ('role_id', models.IntegerField(verbose_name='Роль')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('photo', models.TextField(blank=True, null=True, verbose_name='Фото')),
                ('self_registration', models.BooleanField(blank=True, null=True, verbose_name='Регистрация на сайте')),
                ('password', models.CharField(max_length=250, verbose_name='Пароль')),
                ('date_delete', models.DateField(blank=True, null=True, verbose_name='Дата удаления')),
                ('emp_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.person')),
            ],
        ),
    ]
