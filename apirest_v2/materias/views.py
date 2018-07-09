from django.http import HttpResponse
from rest_framework import generics
from .serializers import materiaSerializer
from .models import materias

from django.shortcuts import render
#from materias.serializers import materiaSerializer, usuarioSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import permissions

def index(request):
    return HttpResponse("<h1>KK EAE JANGUINHO</h1>")


class ListCreateMaterias(generics.ListCreateAPIView):
    queryset = materias.objects.all()
    serializer_class = materiaSerializer



    