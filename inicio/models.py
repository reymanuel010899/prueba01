from django.db import models

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
class celularesmodels(models.Model):
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
    titulo = models.CharField(max_length=300)
    tipo = models.CharField(max_length=50) 
    detalle = models.TextField()
    avatar = models.FileField(upload_to='acesorios')   
    precio = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.tipo
class tablesmodels(models.Model):
    titulo = models.CharField(max_length=300)
    marca = models.CharField(max_length=30)
    avatar = models.FileField(upload_to='tables')   
    detalle = models.TextField()
    almacenamiento = models.CharField(max_length=30)
    precio = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.detalle
class monitoresmodels(models.Model):
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