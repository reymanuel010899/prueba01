from django.db import models


class categora_manayer(models.Manager):
    def obtener_categoria(self , categoria):
        return self.get(categorias__id = categoria)

class electico_maneyer(models.Manager):
    def get_vistas_count(self):
        return self.vistas_set.all().count()       