from django.urls import path
from .views import home, tarea
app_name = 'inicio'

urlpatterns = [
    path('', home, name='inicio'),
    path("tarea", tarea, name="tarea")
]
