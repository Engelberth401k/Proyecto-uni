# Sistema de ventas en Python

1. Descripción del proyecto

Sistema de ventas desarrollado en Python que permite gestionar productos mediante dos tipos de usuarios: vendedores y compradores.

Los vendedores pueden agregar, visualizar y editar productos, mientras que los compradores pueden consultar el catálogo y buscar productos por su nombre.

2. Descripción de los módulos

- **login.py:** permite seleccionar el tipo de usuario y verificar sus credenciales.
- **vendedor.py:** contiene las funciones del menú del vendedor para administrar los productos.
- **comprador.py:** permite visualizar y buscar productos disponibles.
- **inventario.py:** contiene las funciones para agregar, editar, buscar, cargar y guardar productos.
- **test.py:** contiene las pruebas unitarias realizadas mediante assert.
- **productos.json:** almacena los productos y sus precios.

3. Requisitos funcionales

- El sistema debe permitir ingresar como vendedor o comprador.
- El sistema debe verificar el nombre de usuario y la contraseña.
- El vendedor debe poder agregar productos.
- El vendedor debe poder consultar y editar el inventario.
- El comprador debe poder visualizar los productos disponibles.
- El comprador debe poder buscar productos por nombre.
- El sistema debe guardar los cambios realizados en el inventario.

4. Requisitos no funcionales

- El programa debe ser sencillo y fácil de utilizar.
- El código debe estar organizado en módulos independientes.
- El sistema debe validar los datos ingresados por el usuario.
- La aplicación debe ejecutarse utilizando Python.
- Los productos deben conservarse después de cerrar el programa.

5. Estructuras de datos utilizadas

Se utilizan listas y diccionarios de Python para almacenar y organizar los productos, sus nombres y precios.

También se utiliza un archivo JSON para conservar la información del inventario.

6. Herramientas utilizadas

- Python 3.14.
- Visual Studio Code.
- Git y GitHub.
- Archivo JSON para almacenamiento.