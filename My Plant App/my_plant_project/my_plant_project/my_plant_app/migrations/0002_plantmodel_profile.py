# Generated by Django 4.2.2 on 2023-07-01 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
        ('my_plant_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantmodel',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='profile_app.profilemodel'),
            preserve_default=False,
        ),
    ]
