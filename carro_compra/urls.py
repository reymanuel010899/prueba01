from django.urls import path

from .views import agregar_producto_carro

app_name = 'carro_compra'

urlpatterns = [
    path('agregar-producto/<pk>/', agregar_producto_carro, name='agregar-producto')
]
