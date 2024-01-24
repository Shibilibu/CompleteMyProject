# Generated by Django 3.2.20 on 2023-08-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('completemyproject', '0004_auto_20230812_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='Date',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='chat',
            name='Message',
            field=models.CharField(default=1, max_length=120),
        ),
        migrations.AddField(
            model_name='chat',
            name='SendType',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='chat',
            name='Toid',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='chat',
            name='Fromid',
            field=models.IntegerField(default=1),
        ),
    ]