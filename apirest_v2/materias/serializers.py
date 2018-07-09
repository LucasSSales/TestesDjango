from rest_framework import serializers
from materias.models import materias
from django.contrib.auth.models import User

class materiaSerializer(serializers.ModelSerializer) :
    id = serializers.IntegerField(read_only=True)
    class Meta :
        model = materias
        fields = ('id', 'usuario', 'nome', 'ab1', 'ab2', 'reav', 'final', 'media', 'faltas', 'carga_horaria', 'max_faltas', 'conceito')
