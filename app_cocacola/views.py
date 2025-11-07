from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Proveedor
from django.urls import reverse
from django.utils import timezone

def inicio_cocacola(request):
    return render(request, 'inicio.html')

# Agregar cliente (muestra formulario y procesa POST)
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        email = request.POST.get('email', '').strip()
        preferencia = request.POST.get('preferencia', '').strip()
        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            telefono=telefono,
            email=email,
            preferencia=preferencia
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')

# Ver clientes
def ver_cliente(request):
    clientes = Cliente.objects.all().order_by('-fecha_registro')
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

# Mostrar formulario de actualización
def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

# Procesar actualización
def realizar_actualizacion_cliente(request, cliente_id):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=cliente_id)
        cliente.nombre = request.POST.get('nombre', cliente.nombre).strip()
        cliente.apellido = request.POST.get('apellido', cliente.apellido).strip()
        cliente.direccion = request.POST.get('direccion', cliente.direccion).strip()
        cliente.telefono = request.POST.get('telefono', cliente.telefono).strip()
        cliente.email = request.POST.get('email', cliente.email).strip()
        cliente.preferencia = request.POST.get('preferencia', cliente.preferencia).strip()
        cliente.save()
    return redirect('ver_cliente')

# Borrar cliente (confirmación)
def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})


def agregar_proveedor(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get('nombre_empresa', '').strip()
        contacto = request.POST.get('contacto', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        correo = request.POST.get('correo', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        pais = request.POST.get('pais', '').strip()
        tipo_producto_suministro = request.POST.get('tipo_producto_suministro', '').strip()

        Proveedor.objects.create(
            nombre_empresa=nombre_empresa,
            contacto=contacto,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            pais=pais,
            tipo_producto_suministro=tipo_producto_suministro
        )
        return redirect('ver_proveedor')

    return render(request, 'proveedor/agregar_proveedor.html')


def ver_proveedor(request):
    proveedores = Proveedor.objects.all().order_by('-id')
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})


def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


def realizar_actualizacion_proveedor(request, proveedor_id):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        proveedor.nombre_empresa = request.POST.get('nombre_empresa', proveedor.nombre_empresa).strip()
        proveedor.contacto = request.POST.get('contacto', proveedor.contacto).strip()
        proveedor.telefono = request.POST.get('telefono', proveedor.telefono).strip()
        proveedor.correo = request.POST.get('correo', proveedor.correo).strip()
        proveedor.direccion = request.POST.get('direccion', proveedor.direccion).strip()
        proveedor.pais = request.POST.get('pais', proveedor.pais).strip()
        proveedor.tipo_producto_suministro = request.POST.get('tipo_producto_suministro', proveedor.tipo_producto_suministro).strip()
        proveedor.save()
    return redirect('ver_proveedor')


def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})