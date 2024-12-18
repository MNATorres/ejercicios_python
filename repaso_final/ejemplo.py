# Se quiere llevar el control de ventas de productos naturales para el cabello. Para lo cual se procesa la siguiente informacion, que se organiza en arreglos paralelos:
# - numero de factura
# - tipo de producto(shampoo, enjuague, kit)
# - cantidad vendida
# Considerar que el precio del shampoo es  5500, el enjuague 6200 y el kit 10700
# La carga finaliza cuando en numero de factura se ingresa el número -1 o se hayan cargado mas de 30 factura. Considerar que por factura se vende un solo tipo de producto.
# Se pide:
# 1. Validar los tipos de datos
# 2. Mostrar los datos cargados con formato usando una función
# 3. Calcular usando una funcion el promedio en monto vendido(precio total) de facturas en las que se hayan vendido kits
# 4. Calcular el minimo en cantidad vendido usando una funcióin y luego mostrar la información adicional (numero de factura y producto al que corresponde)
# 5. Calcular el porcentaje de shampoo vendido
# 6. Reemplazar en las posiciones que sean menores al promedio, por -1 en el numero de factura y cantidad y un "cambiar precio" en tipo de producto(Usando una funcion)
# 7. Crear una funcion que reciba un tipo de producto y retorne la cantidad total vendida.

def cargar(nroFactura, tipoProducto, cantidadVendida):
    factura = int(input("Ingrese el número de factura: "))
    while factura <= -2 or factura == 0:
        print("Error - El número de factura debe ser mayor a 0")
        factura = int(input("Ingrese el número de factura: "))

    while factura != -1 and len(nroFactura) != 30:
        print("Productos disponibles: shampoo, enjuague, kit")
        producto = input("Ingrese tipo de producto: ").upper()
        while producto != "SHAMPOO" and producto != "ENJUAGUE" and producto != "KIT":
            print("Error - Productos disponibles: shampoo, enjuague, kit")
            producto = input("Ingrese tipo de producto: ").upper()

        cantidad = int(input("Ingrese la cantidad vendida: "))
        while cantidad < 1:
            print("Error - la cantidad vendida no puede ser inferior a 1")
            cantidad = int(input("Ingrese la cantidad vendida: "))
        
        nroFactura.append(factura)
        tipoProducto.append(producto)
        cantidadVendida.append(cantidad)
        
        if len(nroFactura) != 30:
            factura = int(input("Ingrese el número de factura: "))
            while factura <= -2 or factura == 0:
                print("La factura debe tener un número positivo")
                factura = int(input("Ingrese el número de factura: "))

def mostrar(nroFactura, tipoProducto, cantidadVendida):
    print("---Datos---")
    for i in range(len(nroFactura)):
        print(f"Factura: {nroFactura[i]} | Producto: {tipoProducto[i]} | Cantidad: {cantidadVendida[i]}")

def calcularPromedioMontoVendido(tipoProducto, cantidadVendida):
    cont = 0
    acum = 0

    for i in range(len(tipoProducto)):
        if tipoProducto[i] == 'KIT':
            cont += 1
            acum += cantidadVendida[i]

    valorCantidad = acum * 10700
    promedio = valorCantidad / cont

    return promedio

def buscarMinimoVendido(cantidadVendida):
    indexAux = 0
    for i in range(1, len(cantidadVendida)):
        if cantidadVendida[i] < cantidadVendida[indexAux]:
            indexAux = i
    return indexAux    

def calcularPorcentajeShampoo(tipoProducto, cantidadVendida):
    cantShampoo = 0
    cantidaVentas = 0
    for i in range(len(tipoProducto)):
        cantidaVentas += cantidadVendida[i]
        if tipoProducto[i] == 'SHAMPOO':
            cantShampoo += cantidadVendida[i]
    porcentaje = (cantShampoo / cantidaVentas) * 100
    return porcentaje

def reemplazar(nroFactura, tipoProducto, cantidadVendida, promedio):
    for i in range(len(nroFactura)):
        ventas = 0
        if tipoProducto[i] == "SHAMPOO":
            precio = 5500
        elif tipoProducto[i] == "ENJUAGUE":
            precio = 6200
        else:
            precio = 10700  
        
        ventas = cantidadVendida[i] * precio

        if ventas < promedio:
            nroFactura[i] = -1
            cantidadVendida[i] = -1
            tipoProducto[i] = 'cambiar precio'

def calcularCantidadPorProducto(producto, tipoProducto, cantidadVendida):
    cont = 0
    for i in range(len(cantidadVendida)):
        if producto.upper() == tipoProducto[i]:
            cont += cantidadVendida[i]
    return cont

nroFactura = []
tipoProducto = []
cantidadVendida = []
cargar(nroFactura, tipoProducto, cantidadVendida)

if len(nroFactura) > 0:
    mostrar(nroFactura, tipoProducto, cantidadVendida)
    promedioKits = calcularPromedioMontoVendido(tipoProducto, cantidadVendida)
    print(f"El promedio monto vendido de kits {promedioKits}")
    minVendido = buscarMinimoVendido(cantidadVendida)
    print(f"El minimo vendido es {tipoProducto[minVendido]}, facura {nroFactura[minVendido]}, cantidad {cantidadVendida[minVendido]}")
    porcentajeShampoo = calcularPorcentajeShampoo(tipoProducto, cantidadVendida)
    print(f"El porcentaje de shampoo venido es %{porcentajeShampoo}")
    reemplazar(nroFactura, tipoProducto, cantidadVendida, promedioKits)
    mostrar(nroFactura, tipoProducto, cantidadVendida)
    ventas = calcularCantidadPorProducto("shampoo", tipoProducto, cantidadVendida)
else:
    print("No hay datos para mostrar")    