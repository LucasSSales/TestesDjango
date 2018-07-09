from django.http import HttpResponse
from rest_framework import generics
from .serializers import materiaSerializer, usuarioSerializer
from .models import materias

from django.shortcuts import render
#from materias.serializers import materiaSerializer, usuarioSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import permissions

class criarUsuario(generics.CreateAPIView) :
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = usuarioSerializer

#def index(request):
#    return HttpResponse("<h1>KK EAE JANGUINHO</h1>")


class ListCreateMaterias(generics.ListCreateAPIView):
    queryset = materias.objects.all()
    serializer_class = materiaSerializer
    def list(self, request) :
        lista = materias.objects.filter(usuario = request.user)
        serializer = materiaSerializer(lista, many = True)
        return Response(serializer.data)

    def create(self, request) :
        serializer = materiaSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save(usuario = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



    