# Generated by Django 3.2.4 on 2021-06-02 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_person_options'),
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='users.person'),
        ),
        migrations.AlterField(
            model_name='request',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='users.person'),
        ),
    ]
