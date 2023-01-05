from django.db import models
from django.contrib.auth.models import User


ALMACENAR=(
    ('32','32'),
    ('64','64'),
    ('128','128'),
    ('256','256')
)

# Create your models here.
class card_shop(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        titulo = models.CharField(max_length=300, blank=True)
        modelo = models.CharField(max_length=50, blank=True)
        marca = models.CharField(max_length=30, blank=True)
        avatar = models.FileField(upload_to='electronico', blank=True)
        procesador = models.CharField(max_length=50, blank=True) 
        precio = models.CharField(max_length=15, blank=True)
        in_portada = models.BooleanField(default=False)
        tipo = models.CharField(max_length=50, blank=True)
        tamaño = models.CharField(max_length=5, blank=True)
        detalles = models.TextField(blank=True)
        almacenamiento = models.CharField(max_length=3,blank=True, choices=ALMACENAR)
        rating = models.PositiveIntegerField(blank=True)
        created = models.DateTimeField(auto_now_add=True)
        