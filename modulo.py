#Funciones transaccionales / Validadoras
#Funcion para encontrar stock en base a la categoria
def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    encontrado = False
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria.lower():
            total_stock += inventario[codigo][0]
            encontrado = True
    return encontrado, total_stock
#Funcion para validar codigo ingresado
def validar_codigo(codigo, productos):
    if not codigo or " " in codigo:
        return False
    if codigo in productos:
        return False
    return True
#Funcion para buscar productos por rango de precios minimo y maximo 
def buscar_precio(precio_min, precio_max, productos, inventario):
    lista_filtrada = []
    for codigo, datos in productos.items():
        nombre = datos[0]
        precio = datos[2]
        stock = inventario[codigo][0]
        if precio_min <= precio <= precio_max and stock > 0:
            lista_filtrada.append(f"{nombre}--{codigo}")
    lista_filtrada.sort()
    # Retornamos la lista pura
    return lista_filtrada
#Funcion para actualizar los precios, usando el codigo del producto
def actualizar_precio(codigo, nuevo_precio, productos):
    productos[codigo][2] = nuevo_precio
#Funcion para agregar un producto poniendo un codigo
def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    productos[codigo]=[nombre, categoria, precio, disponible]
    inventario[codigo]=[stock, vendidos]
#Funcion para eliminar un producto, usando el codigo
def eliminar_producto(codigo, productos, inventario):
    del productos[codigo]
    del inventario[codigo]
#Funcion para mostrar todos los productos y sus valores
def mostrar_productos(productos, inventario):
    if not productos:
        print("No hay productos registrados en el sistema")
        return
    
    print(f"{"Codigo":<8}{"Nombre":<12}{"Categoria":<12}{"Precio":<8}{"Disp":<6}{"Stock":<6}{"Vendidos":<8}")
    print("-" * 65)
    for codigo, datos in productos.items():
        nombre=datos[0]
        categoria=datos[1]
        precio=datos[2]
        disponible= "Si" if datos[3] else "No"
        
        stock=inventario[codigo][0]
        vendidos=inventario[codigo][1]
        
        print(f"{codigo:<8}{nombre:<12}{categoria:<12}${precio:<7}{disponible:<6}{stock:<6}{vendidos:<8}")
#Funcion de validacion de opcion
def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    except ValueError:
        return 0