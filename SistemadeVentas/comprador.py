# Esto se abre desde el archivo de login.py, corre el codigo desde ahi

from inventario import buscar_producto


def menu_comprador(productos):

    while True:
        print("\n=== MENU COMPRADOR ===")
        print("1. Ver productos")
        print("2. Buscar producto")
        print("3. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            print("\n=== PRODUCTOS DISPONIBLES ===")

            for p in productos:
                print(p["nombre"], "- C$", p["precio"])

            if len(productos) == 0:
                print("No hay productos disponibles.")

        elif opcion == "2":
            nombre = input("Nombre del producto: ").strip()

            encontrados = buscar_producto(productos, nombre)

            if encontrados:
                print("\n=== RESULTADOS ===")

                for p in encontrados:
                    print(p["nombre"], "- C$", p["precio"])

            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            print("Cerrando sesion...")
            break

        else:
            print("Opcion incorrecta.")