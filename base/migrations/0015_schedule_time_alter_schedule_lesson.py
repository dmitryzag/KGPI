# Generated by Django 4.0.4 on 2022-05-01 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_schedule_id_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.time'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.subject'),
        ),
    ]