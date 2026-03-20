from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, LineaPedido
from django.contrib import messages
from django.shortcuts import redirect

from carro.carro import Carro

# Create your views here.

@login_required(login_url='autenticacion/login')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_email(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email,
    )
    
    messages.success(request, "El pedido se ha creado correctamente")
    return redirect('../tienda')
    
def enviar_email(**kwargs):
    pass
    