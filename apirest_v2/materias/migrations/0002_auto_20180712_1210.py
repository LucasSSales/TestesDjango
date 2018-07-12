# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-12 12:10
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materias',
            name='ab1',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='ab2',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='carga_horaria',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='conceito',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='faltas',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='final',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='max_faltas',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='media',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='reav',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='usuario',
        ),
        migrations.AddField(
            model_name='materias',
            name='notas',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]