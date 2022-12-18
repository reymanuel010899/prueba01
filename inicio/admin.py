from django.contrib import admin
from .models import celularesmodels, laptopmodels, acesoriomodels, monitoresmodels, cpumodels, tablesmodels, electronicomodel,categoria
# Register your models here.
admin.site.register(electronicomodel)
admin.site.register(categoria)
admin.site.register(celularesmodels)
admin.site.register(laptopmodels)
admin.site.register(acesoriomodels)
admin.site.register(monitoresmodels)
admin.site.register(cpumodels)
admin.site.register(tablesmodels)
