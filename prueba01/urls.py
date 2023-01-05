
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls', namespace='inicio')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('carro/', include('carro_compra.urls', namespace='carro_compra')),
    path('primera/api/', include('tiendaapi.urls', namespace='tiendaapi'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)