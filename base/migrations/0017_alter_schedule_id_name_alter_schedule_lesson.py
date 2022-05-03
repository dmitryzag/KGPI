# Generated by Django 4.0.4 on 2022-05-01 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_remove_schedule_time_schedule_id_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='id_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.subject'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.time'),
        ),
    ]
