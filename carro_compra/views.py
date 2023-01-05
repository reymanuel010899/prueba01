from django.shortcuts import render, redirect , HttpResponse, HttpResponsePermanentRedirect
from .models import card_shop
from inicio.models import electronicomodel
# Create your views here.

def agregar_producto_carro(request, pk):
      if request.GET['rating'] == None:
            return redirect("inicio:detalle-productos",  pk = pk )


      elif request.method == 'GET':
            productos = electronicomodel.objects.get(id=pk)
            titulo  = productos.titulo
            cantidad = request.GET['rating']
            if  productos.rating > int(cantidad):
                  card_shop.objects.update_or_create(user=request.user,  titulo = titulo ,
                  modelo = productos.modelo, marca=productos.marca, avatar=productos.avatar,
                  procesador=productos.procesador, precio = productos.precio, tipo = productos.tipo,
                  tamaño=productos.tamaño, detalles=productos.detalles, almacenamiento=productos.almacenamiento,
                  rating = cantidad)
                  return render(request, 'carro-compras.html')
            else:
                  context = {
                        'pk': productos.id ,
                        'error':'no hay suficiente producto para esta cantidad'
                  }
                  return redirect("inicio:detalle-productos",  pk = context['pk'], )