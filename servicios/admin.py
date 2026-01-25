from django.contrib import admin
from .models import Servicio

# Register your models here.


class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created', 'updated')


admin.site.register(Servicio, ServicioAdmin)
