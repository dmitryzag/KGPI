# Generated by Django 4.0.4 on 2022-05-03 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_dayofweek_weekparity_remove_schedule_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ('lesson',)},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='teacher',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='patronymic',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='position',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='surname',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subj', to='base.dayofweek'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='parity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weekday', to='base.weekparity'),
        ),
    ]
