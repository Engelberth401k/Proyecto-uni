from inventario import agregar_producto, editar_producto, buscar_producto


# Productos de prueba
productos = [
    {"nombre": "Arroz", "precio": 25},
    {"nombre": "Leche", "precio": 40}
]


# Prueba 1: Agregar producto
agregar_producto(productos, "Pan", 15)

assert len(productos) == 3
assert productos[2]["nombre"] == "Pan"

print("Prueba de agregar: CORRECTA")


# Prueba 2: Editar producto
editar_producto(productos, 0, "Arroz integral", 30)

assert productos[0]["nombre"] == "Arroz integral"
assert productos[0]["precio"] == 30

print("Prueba de editar: CORRECTA")


# Prueba 3: Buscar producto
resultado = buscar_producto(productos, "leche")

assert len(resultado) == 1
assert resultado[0]["nombre"] == "Leche"

print("Prueba de buscar: CORRECTA")


# Prueba 4: Validar errores
try:
    agregar_producto(productos, "", 20)
    assert False

except ValueError:
    print("Prueba de validacion: CORRECTA")


print("\nTodas las pruebas finalizaron correctamente.")