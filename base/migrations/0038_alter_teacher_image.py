# Generated by Django 4.0.4 on 2022-05-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(null=True, upload_to='teachers/'),
        ),
    ]
