from django.urls import path
from .views import listarapiview, listarcategoriaapiview, crearapiview, detalleapis,updateapis

app_name = 'tiendaap'

urlpatterns = [
    path('primera-api/', listarapiview.as_view(), name='primera-api' ),
    path('categoria-api/', listarcategoriaapiview.as_view(), name='categoria-api' ),
    path('crear-api/', crearapiview.as_view(), name='crear-api' ),
    path('detalle-api/<pk>/', detalleapis.as_view(), name='detalle-api' ),
       path('update-api/<pk>/', updateapis.as_view(), name='crear-api' ),
]
