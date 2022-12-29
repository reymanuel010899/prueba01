from django.db import models
from django.contrib.auth.models import User
from .maneger import categora_manayer
class categoria(models.Model):
    nombre = models.CharField(max_length=30)
    objects =categora_manayer()

    def __str__(self):
        return str(self.id) +'-'+ self.nombre

# Create your models here.

ALMACENAR=(
    ('32','32'),
    ('64','64'),
    ('128','128'),
    ('256','256')
)

COLOR = (
    ('R','ROJO'),
    ('N','NEGRO'),
    ('B','BLANCO'),
    ('O','OTROS')
)

class electronicomodel(models.Model):
        categoria = models.ForeignKey(categoria, related_name='categorias', on_delete=models.CASCADE)
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
        

        def __str__(self) -> str:
            return str(self.id) + '-' + self.modelo
        
class celularesmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='celular')
    titulo = models.CharField(max_length=300)
    modelo = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='celulares')   
    precio = models.CharField(max_length=5)
    detalles = models.TextField()
    almacenamiento = models.CharField(max_length=3, choices=ALMACENAR)
    color = models.CharField(max_length=10, choices=COLOR)
    rating = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.modelo

class laptopmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='laptop')
    titulo = models.CharField(max_length=300)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='laptop')   
    precio = models.CharField(max_length=10)
    almacenamiento = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.modelo

class  acesoriomodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='acesorio')
    titulo = models.CharField(max_length=300)
    tipos = models.CharField(max_length=50) 
    detalle = models.TextField()
    avatar = models.FileField(upload_to='acesorios')   
    precio = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.tipos
class tablesmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='table')
    titulo = models.CharField(max_length=300)
    marca = models.CharField(max_length=30)
    avatar = models.FileField(upload_to='tables')   
    detalle = models.TextField()
    almacenamiento = models.CharField(max_length=30)
    precio = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.detalle
class monitoresmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='monitores')
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='tables') 
    precio = models.CharField(max_length=10)
    detalle = models.TextField()
    tamaño = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.model
class cpumodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='cpu')
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='tables') 
    precio = models.CharField(max_length=10)
    detalle = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.model