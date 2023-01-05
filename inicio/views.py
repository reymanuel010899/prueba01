from django.shortcuts import render, redirect
from .models import electronicomodel
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db.models import Q
from .models import categoria
from .models import electronicomodel
from carro_compra.forms import electronicoform
from django.db.models import  Sum
from django.core.paginator import Paginator
from django.views.generic import DetailView
from .models import vistas
# Create your views here.
def home (request):
    #portada = electronicomodel.object.obtener_portada()
    laptops = electronicomodel.objects.all().order_by('created')[:]
    lisa  = electronicomodel.objects.all().filter()
    vista = vistas.objects.all().order_by('created')[:4]
    return render(request, 'index.html',{'laptops':laptops, 'vistas':vista})
    

def electrodomesticosview(request):
    laptop = electronicomodel.objects.all()
    paginator = Paginator(laptop, 3)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page)

    return render(request, 'electronico.html', {'page':page})    

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


class detalle_producto(DetailView):
    template_name = 'detalle-producto.html'
    model = electronicomodel

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context["producto"] = electronicomodel.objects.get(id=pk)
        id_categoria = categoria.objects.obtener_categoria(pk)
        id_categoria = id_categoria.id
        context["lista"] = electronicomodel.objects.filter(categoria__id = id_categoria).exclude(id=pk)[:8]
        context["form"] = electronicoform
        context["cantidad"] =  electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('rating') )
        return context

    def get_object(self, **kwargs):
        object =  super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            vistas.objects.get_or_create(user = self.request.user , articulo = object )   
        return object
   
def detalle_favorito(request, pk):

    producto = electronicomodel.objects.get(electronico__id=pk)
    pk = electronicomodel.objects.get(electronico__id=pk)
    pk = pk.id
    archivo = vistas.objects.get(articulo__id = pk)
    id_categoria = categoria.objects.obtener_categoria(pk)
    id_categoria = id_categoria.id
    lista = electronicomodel.objects.filter(categoria__id = id_categoria).exclude(id=pk)[:8]
    form = electronicoform
    cantidad =  electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('rating') )
    return render(request, 'detalle-favorito.html',{"datalle":archivo, 'productos':producto, 'cantidad':cantidad , 'form':form, 'lista':lista})


