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
                categoria_buscar = input("Ingrese la categoria del producto (Accesorios/Papelería): ").strip()
                
                encontrado, total = me.stock_categoria(categoria_buscar, productos, inventario)
                if encontrado:
                    print(f"\nEl stock total para la categoría '{categoria_buscar}' es: {total}")
                else:
                    print(f"\nNo se encontraron productos en la categoría '{categoria_buscar}'.")
                os.system("pause")
            case "2":
                os.system("cls")
                print("Buscar productos por rango de precios")
                try:
                    precio_min = int(input("Ingrese el precio minimo: "))
                    precio_max = int(input("Ingrese el precio maximo: "))
                    
                    resultados = me.buscar_precio(precio_min, precio_max, productos, inventario)
                    if resultados:
                        print(f"\nProductos encontrados entre ${precio_min} y ${precio_max}:")
                        for item in resultados:
                            print(item)
                    else:
                        print("\nNo se han encontrado productos disponibles en ese rango de precios.")
                except ValueError:
                    print("\n[ERROR]: Debe ingresar valores numéricos adecuados.")
                os.system("pause")
            case "3":
                os.system("cls")
                print("Actualizar precios de un producto")
                codigo=input("ingrese el codigo del producto (ej:P0101): ").strip().upper()
                if codigo in productos:
                    try:
                        nuevo_precio=int(input("Ingrese el nuevo precio: "))
                        me.actualizar_precio(codigo, nuevo_precio, productos)
                    except ValueError:
                        print("\n[Error]: El precio debe ser un valor numerico entero")
                else:
                    print("\n[ERROR]: El codigo ingresado no existe en el sistema")
                os.system("pause")
            case "4":
                os.system("cls")
                print("Agregar producto")
                codigo=input("Ingrese nuevo codigo (ej P105):").strip().upper()
                if me.validar_codigo(codigo, productos):
                    print("¡Codigo validado!, ingrese los datos del producto")
                    nombre=input("Ingrese el nombre: ").strip()
                    categoria=input("Ingrese categoria (Accesorios/Papelería): ").strip()
                    try:
                        precio=int(input("Ingrese el precio: "))
                        
                        disp_input=input("¿Esta disponible? (s/n): ").strip().lower()
                        disponible =True if disp_input == "s" else False
                        
                        stock= int(input("Ingrese el stock inicial: "))
                        vendidos= int(input("Ingrese las unidades vendidas: "))
                        
                        me.agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario)
                        print("\n¡Producto registrado y agregado al inventario con exito!")
                    except ValueError:
                        print("\n[ERROR]: El precio, stock y vendidos deben ser numeros enteros")
                else:
                    print("ERROR, el codigo esta con espacios o ya existe")
                os.system("pause")
            case "5":
                os.system("cls")
                print("Eliminar producto")
                codigo=input("Ingrese el codigo del producto a eliminar: ").strip().upper()
                if codigo in productos:
                    me.eliminar_producto(codigo, productos, inventario)
                    print(f"\n¡El producto {codigo} ha sido eliminado correctamente!")
                else:
                    print("\n[ERROR]: El codigo ingresado no existe en el sistema")
                os.system("pause")
            case "6":
                os.system("cls")
                print("Listado de productos en el sistema")
                me.mostrar_productos(productos, inventario)
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