# Generated by Django 4.0.4 on 2022-05-01 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_remove_week_week_delete_day_delete_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
    ]