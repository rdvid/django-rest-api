# Generated by Django 3.0.7 on 2023-01-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
