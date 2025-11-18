# TODO: Agregar Tablas Producto y Proveedor

## Información Recopilada
- Proyecto Django con modelos Cliente, Empleado, Orden.
- Barra de navegación en base.html con botones para Inicio, Empleados, Clientes, Órdenes.
- Estructura de vistas, URLs y templates existente para CRUD.
- CSS existente en static/css/styles.css.

## Plan Detallado
- Agregar modelos Producto y Proveedor en models.py con campos especificados y relaciones ForeignKey.
- Registrar modelos en admin.py.
- Agregar botones "Productos" y "Proveedores" en la barra de navegación de base.html.
- Crear vistas CRUD para Producto y Proveedor en views.py.
- Agregar URLs para Producto y Proveedor en urls.py.
- Crear directorios de templates: templates/producto/ y templates/proveedor/.
- Crear templates para ver, agregar, actualizar, borrar Producto y Proveedor, siguiendo la estructura de cliente y empleado.
- Ejecutar migraciones para crear las tablas en la base de datos.

## Pasos a Completar
- [x] Agregar modelos Producto y Proveedor en models.py
- [x] Registrar modelos en admin.py
- [x] Agregar botones en base.html
- [x] Crear vistas para Producto en views.py
- [x] Crear vistas para Proveedor en views.py
- [x] Agregar URLs para Producto en urls.py
- [x] Agregar URLs para Proveedor en urls.py
- [x] Crear templates para Producto (ver, agregar, actualizar, borrar)
- [x] Crear templates para Proveedor (ver, agregar, actualizar, borrar)
- [x] Ejecutar makemigrations y migrate
