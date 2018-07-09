# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import materias

# Register your models here.

@admin.register(materias)
class materiasAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nome', 'ab1', 'ab2', 'reav', 'final', 'media', 'faltas', 'carga_horaria', 'max_faltas', 'conceito')
    #'created_at', 'modified_at')
