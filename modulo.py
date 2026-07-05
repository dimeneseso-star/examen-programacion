def stock_categoria(categoria, productos, inventario):
    total_stock=0
    encontrado=False
    
    for codigo, datos in productos.items():
        if datos[1].lower()==categoria.lower():
            total_stock += inventario[codigo][0]
            encontrado=True
            
    if encontrado: 
        print(f"\n El stock total para la categoría '{categoria}' es: {total_stock}")
    else:
        print(f"\nNo se encontraron productos en la categoría '{categoria}'.")
        
def validar_codigo(codigo, productos):
    if not codigo or " " in codigo:
        return False
    if codigo in productos:
        return False
    return True
def buscar_precio(precio_min, precio_max, productos, inventario):
    lista_filtrada = []
    
    for codigo, datos in productos.items():
        nombre= datos[0]
        precio= datos[2]
        stock=inventario[codigo][0]
        
        if precio_min <= precio <= precio_max and stock > 0:
            lista_filtrada.append(f"{nombre}--{codigo}")
            
    lista_filtrada.sort()
    
    
    if lista_filtrada:
        print(f"\nProductos encontrados entre ${precio_min} y ${precio_max}")
        for item in lista_filtrada:
            print(item)
            
    else:
        print("\nNo se a encontrado productos disponibles en ese rango de precios")

def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    except ValueError:
        return 0