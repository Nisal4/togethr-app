# Generated by Django 4.2.7 on 2023-11-28 16:01

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_profile_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]