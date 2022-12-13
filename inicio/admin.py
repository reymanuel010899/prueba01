from django.contrib import admin
from .models import celularesmodels, laptopmodels, acesoriomodels, monitoresmodels, cpumodels, tablesmodels
# Register your models here.
admin.site.register(celularesmodels)
admin.site.register(laptopmodels)
admin.site.register(acesoriomodels)
admin.site.register(monitoresmodels)
admin.site.register(cpumodels)
admin.site.register(tablesmodels)