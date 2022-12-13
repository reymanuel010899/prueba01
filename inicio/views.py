from django.shortcuts import render
from .models import celularesmodels, laptopmodels, acesoriomodels, monitoresmodels, cpumodels, tablesmodels

# Create your views here.
def home (request):
    return render(request, 'index.html')
    
def electrodomesticosview(request):
    celulares = celularesmodels.objects.all()
    laptop = laptopmodels.objects.all()
    acesorio = acesoriomodels.objects.all()
    monitores = monitoresmodels.objects.all()
    cpu = cpumodels.objects.all()
    tables = tablesmodels.objects.all()
    context = {
        'celulares':celulares,
        'laptops':laptop,
        'acesorios':acesorio,
        'monitores':monitores,
        'cpus':cpu,
        'tables':tables
    }
    

    return render(request, 'electronico.html',context)    