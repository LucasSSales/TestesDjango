# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-12 17:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materias', '0002_auto_20180712_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='materias',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='materias', to=settings.AUTH_USER_MODEL),
        ),
    ]