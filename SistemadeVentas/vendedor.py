# Esto se abre desde el archivo login.py, corre el codigo desde ahi

from inventario import agregar_producto, editar_producto, guardar_productos

def menu_vendedor(productos):

    while True:
        print("\n=== MENU VENDEDOR ===")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Editar producto")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))

                agregar_producto(productos, nombre, precio)
                guardar_productos(productos)

                print("Producto agregado correctamente.")

            except ValueError as error:
                print("Error:", error)

        elif opcion == "2":
            print("\n=== INVENTARIO ===")

            for i, p in enumerate(productos, 1):
                print(i, p["nombre"], "- C$", p["precio"])

            if len(productos) == 0:
                print("Inventario vacío.")

        elif opcion == "3":
            if len(productos) == 0:
                print("No hay productos para editar.")
                continue

            for i, p in enumerate(productos, 1):
                print(i, p["nombre"], "- C$", p["precio"])

            try:
                numero = int(input("Numero a editar: ")) - 1

                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))

                editar_producto(productos, numero, nombre, precio)
                guardar_productos(productos)

                print("Producto editado correctamente.")

            except ValueError as error:
                print("Error:", error)

        elif opcion == "4":
            print("Cerrando sesion...")
            break

        else:
            print("Opcion incorrecta.")