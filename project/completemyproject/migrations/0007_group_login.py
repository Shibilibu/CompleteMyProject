# Generated by Django 3.2.20 on 2023-09-05 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('completemyproject', '0006_auto_20230821_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='Login',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='completemyproject.login'),
        ),
    ]
