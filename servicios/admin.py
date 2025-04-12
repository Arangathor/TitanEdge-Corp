from django.contrib import admin
from .models import Servicio, CategoriaServicio

# Admin personalizado para Servicio
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("titulo", "categoria", "created")
    list_filter = ("categoria",)
    search_fields = ("titulo",)

# Admin simple para Categoría
class CategoriaServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

# Registro de modelos
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(CategoriaServicio, CategoriaServicioAdmin)
