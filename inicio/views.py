from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'index.html')
    
def tarea(request):
    return render(request, 'tarea.html')    