#from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class materias(models.Model) :
    usuario = models.ForeignKey('auth.User', related_name= 'materias', on_delete=models.CASCADE, default = 1)
    nome = models.CharField(max_length=200)
    ab1 = models.DecimalField(max_digits=6, decimal_places=2)
    ab2 = models.DecimalField(max_digits=6, decimal_places=2)
    reav = models.DecimalField(max_digits=6, decimal_places=2)
    final = models.DecimalField(max_digits=6, decimal_places=2)
    media = models.DecimalField(max_digits=6, decimal_places=2)
    faltas = models.IntegerField()    
    carga_horaria = models.IntegerField()
    max_faltas = models.IntegerField()
    conceito = models.CharField(max_length=200)

'''
class materias(models.Model) :
    usuario = models.ForeignKey('auth.User', related_name= 'materias', on_delete=models.CASCADE, default = 1)
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    max_faltas = models.IntegerField()
    faltas = models.IntegerField()  
    conceito = models.CharField(max_length=200)
    notas = JSONField()
    #ex: notas = {'ab1': 0.0, 'ab2': 0.0, 'reav': 0.0, 'final': 0.0, 'media': 0.0}   

'''

