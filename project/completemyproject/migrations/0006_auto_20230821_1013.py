# Generated by Django 3.2.20 on 2023-08-21 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('completemyproject', '0005_auto_20230812_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='Fromid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='completemyproject.internguide'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='Toid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='completemyproject.externalguide'),
        ),
    ]
