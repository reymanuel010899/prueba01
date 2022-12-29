from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import celularesmodels, laptopmodels, acesoriomodels, monitoresmodels, cpumodels, tablesmodels,electronicomodel
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.db.models import Q
from .models import categoria
from .models import electronicomodel
from .forms import electronicoform
from django.db.models import Count, Sum
# Create your views here.
def home (request):
    #portada = electronicomodel.object.obtener_portada()
    laptops = laptopmodels.objects.all().order_by('created')[:3]
    return render(request, 'index.html',{'laptops':laptops})
    

def electrodomesticosview(request):
    celulares = celularesmodels.objects.all()
    laptop = laptopmodels.objects.all()
    acesorio = acesoriomodels.objects.all()
    monitores = monitoresmodels.objects.all()
    cpu = cpumodels.objects.all()
    tables = tablesmodels.objects.all()
   
    return render(request, 'electronico.html',{'laptops':laptop})    

def iniciarsecionview(request):
    if request.method == 'GET':
        return render(request, 'iniciar_secion.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            return  render(request, 'iniciar_secion.html', {'error':'esta cuenta no existe'})
        else:    
            return redirect('inicio:inicio')


def registrar_user(request):
    if request.method == 'GET':
        return render(request, 'registraruser.html')
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'registraruser.html', {'error':'contraseñas invalidas'} )
        else:
            username = request.POST['username']
            try:
                user = User.objects.create_user(username=username, password=request.POST['password1'])
                login(request, user)
                return redirect('inicio:inicio')
            except:
                 return render(request, 'registraruser.html', {'error':'username already exist'} )
     
def busqueda_contenido(request):
    contenido = request.GET.get('contenido').upper()
    url = request.GET.get('url')
    if url == 'electronicos':
        electrico = electronicomodel.objects.filter(Q(titulo__icontains= contenido) | Q(modelo__icontains = contenido) )
        return render(request, 'busqueda.html', {"electronicos":electrico})
    elif url == 'hombres': 
        pass
    elif url == 'mujer':
        pass
    elif url == 'niños':
        pass
    elif url == 'electrodomesticos':
        pass
    elif url == 'deportes':
        pass
    else:
        electrico = electronicomodel.objects.filter(Q(titulo__icontains= contenido) | Q(modelo__icontains = contenido) )
        return render(request, 'busqueda.html', {"electronicos":electrico})

def detalle_productos(request, pk):
    producto = electronicomodel.objects.get(id=pk)
    id_categoria = categoria.objects.obtener_categoria(pk)
    id_categoria = id_categoria.id
    lista_productos = electronicomodel.objects.filter(categoria__id = id_categoria).exclude(id=pk)[:8]
    cantidad = electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('rating') )
    if request.method == 'GET':
        id_producto = request.GET.get('productoid')
        productos = electronicomodel.objects.filter(id=id_producto)
        #carro_compra.objects.update_or_create(titulo = productos.titulo , modelo = productos.modelo )
    print(id_producto)
    return render(request, 'detalle-producto.html', {'producto':producto, 'lista':lista_productos, 'form':electronicoform, 'cantidad':cantidad})
    