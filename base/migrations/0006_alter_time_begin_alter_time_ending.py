# Generated by Django 4.0.4 on 2022-04-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='begin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='time',
            name='ending',
            field=models.DateTimeField(),
        ),
    ]