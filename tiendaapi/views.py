from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from inicio.models import electronicomodel,categoria
from .serializers import serialisarmodelo, categoriaserial, paginacion, crearserializar, actualizar
# Create your views here.


class listarapiview(ListAPIView):
    serializer_class = serialisarmodelo
    pagination_class = paginacion

    def get_queryset(self):
        return electronicomodel.objects.all()
    

class listarcategoriaapiview(ListAPIView):
    serializer_class =    categoriaserial

    def get_queryset(self):
        return categoria.objects.all()
    
class crearapiview(CreateAPIView):
    serializer_class = crearserializar

class detalleapis(RetrieveAPIView):
    serializer_class = actualizar
    queryset = electronicomodel

class  updateapis(UpdateAPIView):
    serializer_class = actualizar
    queryset = electronicomodel
