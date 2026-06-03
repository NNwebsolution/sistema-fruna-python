productos = []
total = 0

continuar = "aparte"

while continuar == "aparte":

    nombre = input("Ingrese el producto: ")

    precio = float(input("Ingrese precio del producto: "))

    producto = {
        "nombre": nombre,
        "precio": precio
    }

    productos.append(producto)

    continuar = input("Escriba 'aparte' para seguir o 'ahinomas' para terminar: ")

    while continuar != "aparte" and continuar != "ahinomas":
        print("Sistema no reconoce esa palabra")
        continuar = input("Escriba 'aparte' para seguir o 'ahinomas' para terminar: ")

print("PRODUCTOS INGRESADOS")

for producto in productos:
    print("Nombre:", producto["nombre"])
    print("Precio:", producto["precio"])
    total = total + producto["precio"]

print("Total:", total)