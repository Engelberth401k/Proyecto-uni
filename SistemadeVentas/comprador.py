# Esto se abre desde el archivo de login.py, corre el codigo desde ahi

def menu_comprador(productos):
    while True:
        print("\n=== MENU DEL COMPRADOR ===")
        print("1. Ver productos")
        print("2. Buscar producto")
        print("3. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("\n=== PRODUCTOS DISPONIBLES ===")

            if len(productos) == 0:
                print("No hay productos disponibles.")
            else:
                for producto in productos:
                    print(
                        producto["nombre"],
                        "- C$", producto["precio"]
                    )

        elif opcion == "2":
            nombre = input(
                "Ingrese el nombre del producto: "
            ).strip().lower()

            encontrados = []

            for producto in productos:
                if nombre in producto["nombre"].lower():
                    encontrados.append(producto)

            if encontrados:
                print("\n=== RESULTADOS ===")
                for producto in encontrados:
                    print(
                        producto["nombre"],
                        "- C$", producto["precio"]
                    )
            else:
                print("No se encontro ese producto.")

        elif opcion == "3":
            print("Cerrando sesion...")
            break

        else:
            print("Opcion incorrecta.")