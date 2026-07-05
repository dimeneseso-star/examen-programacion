import modulo as me
import os
def main():
    os.system("cls")
    # Diccionario productos: [nombre, categoría, precio, disponible]
    productos = {
    "P101": ["Cuaderno", "Papelería", 2490, True],
    "P102": ["Lápiz", "Papelería", 590, True],
    "P103": ["Botella", "Accesorios", 6990, False],
    "P104": ["Mochila", "Accesorios", 24990, True]
    }
    inventario = {
    "P101": [30, 15],
    "P102": [120, 50],
    "P103": [0, 10],
    "P104": [8, 25]
    }
    while True:
        opcion=(input("""
        ============== MENÚ PRINCIPAL =================
        1. Stock por categoría
        2. Buscar productos por rango de precio
        3. Actualizar precio
        4. Agregar producto
        5. Eliminar producto
        6. Mostrar productos
        7. Salir
        ===============================================
        Ingrese una opcion: """)).strip()
        match (opcion):
            case "1":
                os.system("cls")
                print("Buscar stock por categoria")
                categoria_buscar = str(input("Ingrese la categoria del producto (Accesorios/Papelería):"))
                me.stock_categoria(categoria_buscar, productos, inventario)
                os.system("pause")
            case "2":
                os.system("cls")
                print("Buscar productos por rango de precios")
                try:
                    precio_min=int(input("Ingrese el precio minimo: "))
                    precio_max=int(input("Ingrese el precio maximo: "))
                    me.buscar_precio(precio_min, precio_max, productos, inventario)
                except ValueError:
                    print("\n[ERROR]: debe ingresar valores numericos adecuados")
                os.system("pause")
            case "3":
                os.system("cls")
                
                os.system("pause")
            case "4":
                os.system("cls")
                print("Agregar producto")
                codigo=input("Ingrese nuevo codigo (ej P105):").strip().upper()
                if me.validar_codigo(codigo, productos):
                    print("¡Codigo validado!, ingrese los datos del producto")
                else:
                    print("ERROR, el codigo esta con espacios o ya existe")
                os.system("pause")
            case "5":
                os.system("cls")
                
                os.system("pause")
            case "6":
                os.system("cls")
                
                os.system("pause")
            case "7":
                os.system("cls")
                print("Cerrando aplicacion....")
                break
            case _:
                os.system("cls")
                print(" <<< Debe seleccionar una opción válida... >>> ")
                os.system("pause")
if __name__ == "__main__":
    main()