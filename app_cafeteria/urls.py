from django.urls import path
from . import views

urlpatterns = [
    # Cliente URLs
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver_cliente/', views.ver_cliente, name='ver_cliente'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('borrar_cliente/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # Empleado URLs
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('ver_empleado/', views.ver_empleado, name='ver_empleado'),
    path('actualizar_empleado/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('borrar_empleado/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # Orden URLs
    path('agregar_orden/', views.agregar_orden, name='agregar_orden'),
    path('ordenes/', views.ver_ordenes, name='ver_ordenes'),
    path('actualizar_orden/<int:id>/', views.actualizar_orden, name='actualizar_orden'),
    path('borrar_orden/<int:id>/', views.borrar_orden, name='borrar_orden'),

    # Producto URLs
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('ver_producto/', views.ver_producto, name='ver_producto'),
    path('actualizar_producto/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('borrar_producto/<int:id>/', views.borrar_producto, name='borrar_producto'),

    # Proveedor URLs
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('ver_proveedor/', views.ver_proveedor, name='ver_proveedor'),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('borrar_proveedor/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # Inicio URL
    path('', views.inicio, name='inicio'),
]
