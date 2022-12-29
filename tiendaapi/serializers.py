from rest_framework import serializers, pagination
from inicio.models import electronicomodel, categoria

class categoriaserial(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('nombre',)


class serialisarmodelo(serializers.HyperlinkedModelSerializer):
    categoria = categoriaserial()
    class Meta:
        model = electronicomodel
        fields = (  'id',
                    'titulo',
                    'modelo',
                    'marca',
                    'procesador',
                    'precio',
                    'avatar',
                    'almacenamiento',
                    'categoria'
                )
        extra_field = {
            'categoria': {

                'view_name':'inicio:detalle-productos', 'lookup':'pk'
            }

        }


class paginacion(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 10

class crearserializar(serializers.ModelSerializer):
    class Meta:
        model = electronicomodel
        fields = (

            'titulo',
            'almacenamiento',
            'avatar',
            'rating',
            'categoria'
        )  

class actualizar(serializers.ModelSerializer):
    class Meta:
        model = electronicomodel
        fields = ('titulo',
        'modelo','marca',
        'categoria','rating','avatar')        