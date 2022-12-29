from django.db import models

class categora_manayer(models.Manager):
    def obtener_categoria(self , categoria):
        return self.get(categorias__id = categoria)