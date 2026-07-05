def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    encontrado = False
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria.lower():
            total_stock += inventario[codigo][0]
            encontrado = True
    return encontrado, total_stock
        
def validar_codigo(codigo, productos):
    if not codigo or " " in codigo:
        return False
    if codigo in productos:
        return False
    return True
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
        
def actualizar_precio(codigo, nuevo_precio, productos):
    productos[codigo][2] = nuevo_precio
def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    productos[codigo]=[nombre, categoria, precio, disponible]
    inventario[codigo]=[stock, vendidos]
def eliminar_producto(codigo, productos, inventario):
    del productos[codigo]
    del inventario[codigo]
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

def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    except ValueError:
        return 0