# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-09 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0007_auto_20190309_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='control',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
