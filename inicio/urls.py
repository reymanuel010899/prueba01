from django.urls import path
from .views import home, electrodomesticosview,iniciarsecionview, registrar_user,busqueda_contenido, detalle_productos
app_name = 'inicio'

urlpatterns = [
    path('', home, name='inicio'),
    path("electrodomesticos/", electrodomesticosview, name="electrodomesticos"),
    path('identificate/', iniciarsecionview, name='identificate'),
    path('registrate/', registrar_user, name='registrate'),
    path('busqueda-contenido/', busqueda_contenido, name='busqueda-contenido'),
    path('detalle-productos/<pk>/', detalle_productos, name='detalle-productos')
]
