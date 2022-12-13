from django.urls import path
from .views import home, electrodomesticosview
app_name = 'inicio'

urlpatterns = [
    path('', home, name='inicio'),
    path("electrodomesticos/", electrodomesticosview, name="electrodomesticos")
]
