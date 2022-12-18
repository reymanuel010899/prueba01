from django.urls import path
from .views import home, electrodomesticosview,iniciarsecionview, registrar_user,busqueda_contenido
app_name = 'inicio'

urlpatterns = [
    path('', home, name='inicio'),
    path("electrodomesticos/", electrodomesticosview, name="electrodomesticos"),
    path('identificate/', iniciarsecionview, name='identificate'),
    path('registrate/', registrar_user, name='registrate'),
    path('busqueda-contenido/', busqueda_contenido, name='busqueda-contenido')
]
