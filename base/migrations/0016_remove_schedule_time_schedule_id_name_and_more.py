# Generated by Django 4.0.4 on 2022-05-01 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_schedule_time_alter_schedule_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='id_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.subject'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.time'),
        ),
    ]