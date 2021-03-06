# Generated by Django 4.0.4 on 2022-05-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_time_begin_alter_time_ending'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='speciality',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
