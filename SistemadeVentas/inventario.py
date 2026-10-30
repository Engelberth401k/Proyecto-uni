import json
import os

# Productos iniciales
productos_iniciales = [
    {"nombre": "Arroz", "precio": 25},
    {"nombre": "Leche", "precio": 40},
    {"nombre": "Pan", "precio": 15},
    {"nombre": "Aceite", "precio": 65}
]

# Cargar productos
def cargar_productos():
    if not os.path.exists("productos.json"):
        guardar_productos(productos_iniciales)
        return productos_iniciales.copy()

    try:
        with open("productos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except (json.JSONDecodeError, OSError):
        print("Error al cargar los productos.")
        return productos_iniciales.copy()


# Guardar productos
def guardar_productos(productos):
    with open("productos.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)


# Agregar producto
def agregar_producto(productos, nombre, precio):
    nombre = nombre.strip()
    precio = float(precio)

    if nombre == "":
        raise ValueError("El nombre no puede estar vacío.")

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    productos.append({
        "nombre": nombre,
        "precio": precio
    })

    return productos


# Editar producto
def editar_producto(productos, numero, nombre, precio):
    if numero < 0 or numero >= len(productos):
        raise ValueError("Producto no encontrado.")

    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío.")

    precio = float(precio)

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    productos[numero]["nombre"] = nombre
    productos[numero]["precio"] = precio

    return productos


# Buscar producto
def buscar_producto(productos, nombre):
    return [
        p for p in productos
        if nombre.lower() in p["nombre"].lower()
    ]