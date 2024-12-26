import sqlite3
from colorama import init, fore, Back
import os

def limpiar_terminal():
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
init(autoreset=True)

# Crear tabla de productos si no existe
def crear_tabla_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        descripcion TEXT,
                        precio REAL NOT NULL,
                        stock INTEGER NOT NULL)''')
    conexion.commit()
    conexion.close()


# Agregar un producto a la base de datos
def agregar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de stock: "))

    cursor.execute("INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
                   (nombre, descripcion, precio, stock))
    conexion.commit()
    conexion.close()
    print("Producto agregado exitosamente.\n")


# Mostrar todos los productos
def mostrar_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print("\nProductos registrados:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Precio: ${producto[3]}, Stock: {producto[4]}")
    else:
        print("No hay productos registrados.\n")


# Actualizar stock de un producto
def actualizar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nuevo_stock = int(input("Ingrese la nueva cantidad de stock: "))

    cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, id_producto))
    conexion.commit()
    conexion.close()
    print("Stock actualizado exitosamente.\n")


# Eliminar un producto
def eliminar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    conexion.close()
    print("Producto eliminado exitosamente.\n")


# Reporte de productos con bajo stock
def reporte_bajo_stock():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    limite = int(input("Ingrese el límite de stock para el reporte: "))

    cursor.execute("SELECT * FROM productos WHERE stock < ?", (limite,))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print("\nProductos con bajo stock:")
        for producto in productos:
            print(f"Nombre: {producto[1]}, Stock: {producto[4]}")
    else:
        print("No hay productos con bajo stock.\n")

def buscar_producto():
    print("Buscar Productos")
    print("==============\n")
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    nombre = input("Nombre del Producto: ")
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    print("Nombre:", resultado[1], "Precio:", resultado[2], "Descripción:", resultado[3], "Categoría:", resultado[4], "Stock:", resultado[5])    
    conexion.close()
    
    
# Menú principal
def menu():
    crear_tabla_producto()  # Crear la tabla al iniciar el programa
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar productos")
        print("2. Mostrar los productos registrados")
        print("3. Actualizar cantidad de un producto")
        print("4. Eliminar un producto")
        print("5. Reporte de productos con bajo stock")
        print("6. buscar producto")
        print("7. Salir")

        opcion = input("Ingrese un número: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")
            
            # Iniciar programa
if __name__ == "__main__":
    menu()
            
            