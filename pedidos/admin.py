from django.contrib import admin

from .models import LineaPedido, Pedido

# Register your models here.


class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'user', 'created_at')


class LineaPedidoAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'user', 'cantidad', 'created_at')


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido, LineaPedidoAdmin)
