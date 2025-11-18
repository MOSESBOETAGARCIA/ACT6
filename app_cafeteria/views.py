from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado, Orden, Producto, Proveedor

# ==========================================
# VISTAS PARA CLIENTE
# ==========================================

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        fecha_ingreso = request.POST['fecha_ingreso']
        domicilio = request.POST['domicilio']
        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            fecha_ingreso=fecha_ingreso,
            domicilio=domicilio
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')

def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.fecha_nacimiento = request.POST['fecha_nacimiento']
        cliente.correo = request.POST['correo']
        cliente.telefono = request.POST['telefono']
        cliente.fecha_ingreso = request.POST['fecha_ingreso']
        cliente.domicilio = request.POST['domicilio']
        cliente.save()
        return redirect('ver_cliente')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ==========================================
# VISTAS PARA EMPLEADO
# ==========================================

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']
        fecha_ingreso = request.POST['fecha_ingreso']
        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            domicilio=domicilio,
            fecha_ingreso=fecha_ingreso
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')

def ver_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.fecha_nacimiento = request.POST['fecha_nacimiento']
        empleado.correo = request.POST['correo']
        empleado.telefono = request.POST['telefono']
        empleado.domicilio = request.POST['domicilio']
        empleado.fecha_ingreso = request.POST['fecha_ingreso']
        empleado.save()
        return redirect('ver_empleado')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ==========================================
# VISTAS PARA ORDEN
# ==========================================

def agregar_orden(request):
    if request.method == 'POST':
        fecha_orden = request.POST['fecha_orden']
        total = request.POST['total']
        metodo_pago = request.POST['metodo_pago']
        fecha_pago = request.POST['fecha_pago']
        sucursal = request.POST['sucursal']
        id_empleado = request.POST['id_empleado']
        id_cliente = request.POST['id_cliente']
        Orden.objects.create(
            fecha_orden=fecha_orden,
            total=total,
            metodo_pago=metodo_pago,
            fecha_pago=fecha_pago,
            sucursal=sucursal,
            id_empleado_id=id_empleado,
            id_cliente_id=id_cliente
        )
        return redirect('ver_ordenes')
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'orden/agregar_orden.html', {'empleados': empleados, 'clientes': clientes})

def ver_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'orden/ver_ordenes.html', {'ordenes': ordenes})

def actualizar_orden(request, id):
    orden = get_object_or_404(Orden, id_orden=id)
    if request.method == 'POST':
        orden.fecha_orden = request.POST['fecha_orden']
        orden.total = request.POST['total']
        orden.metodo_pago = request.POST['metodo_pago']
        orden.fecha_pago = request.POST['fecha_pago']
        orden.sucursal = request.POST['sucursal']
        orden.id_empleado_id = request.POST['id_empleado']
        orden.id_cliente_id = request.POST['id_cliente']
        orden.save()
        return redirect('ver_ordenes')
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'orden/actualizar_orden.html', {'orden': orden, 'empleados': empleados, 'clientes': clientes})

def borrar_orden(request, id):
    orden = get_object_or_404(Orden, id_orden=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('ver_ordenes')
    return render(request, 'orden/borrar_orden.html', {'orden': orden})

# ==========================================
# VISTAS PARA PRODUCTO
# ==========================================

def agregar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST['nombre_producto']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        disponible = request.POST.get('disponible') == 'on'
        id_proveedor = request.POST.get('id_proveedor') or None
        Producto.objects.create(
            nombre_producto=nombre_producto,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            disponible=disponible,
            id_proveedor_id=id_proveedor
        )
        return redirect('ver_producto')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def ver_producto(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_producto.html', {'productos': productos})

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id_productos=id)
    if request.method == 'POST':
        producto.nombre_producto = request.POST['nombre_producto']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.categoria = request.POST['categoria']
        producto.disponible = request.POST.get('disponible') == 'on'
        producto.id_proveedor_id = request.POST.get('id_proveedor') or None
        producto.save()
        return redirect('ver_producto')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id_productos=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# ==========================================
# VISTAS PARA PROVEEDOR
# ==========================================

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre_proveedor = request.POST['nombre_proveedor']
        cantidad = request.POST['cantidad']
        precio = request.POST['precio']
        total = request.POST['total']
        id_producto = request.POST.get('id_producto') or None
        Proveedor.objects.create(
            nombre_proveedor=nombre_proveedor,
            cantidad=cantidad,
            precio=precio,
            total=total,
            id_producto_id=id_producto
        )
        return redirect('ver_proveedor')
    productos = Producto.objects.all()
    return render(request, 'proveedor/agregar_proveedor.html', {'productos': productos})

def ver_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    if request.method == 'POST':
        proveedor.nombre_proveedor = request.POST['nombre_proveedor']
        proveedor.cantidad = request.POST['cantidad']
        proveedor.precio = request.POST['precio']
        proveedor.total = request.POST['total']
        proveedor.id_producto_id = request.POST.get('id_producto') or None
        proveedor.save()
        return redirect('ver_proveedor')
    productos = Producto.objects.all()
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor, 'productos': productos})

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ==========================================
# VISTA PARA INICIO
# ==========================================

def inicio(request):
    return render(request, 'inicio.html')
