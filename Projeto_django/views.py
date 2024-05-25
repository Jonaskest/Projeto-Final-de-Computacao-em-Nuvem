from django.shortcuts import render

def fazer_pedido(request):
    return render(request, 'fazer_pedido.html')