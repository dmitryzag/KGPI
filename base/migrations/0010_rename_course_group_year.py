# Generated by Django 4.0.4 on 2022-05-01 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_faculty_slug_group_slug_schedule_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='course',
            new_name='year',
        ),
    ]