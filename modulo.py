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

def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    except ValueError:
        return 0