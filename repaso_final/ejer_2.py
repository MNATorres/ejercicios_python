# Se quiere llevar el control de ventas de dos productos: tazas y termos. Se guardan
# las cantidades vendidas en una semana (7 días). Para ello se cargan dos arreglos,
# uno por cada producto. Las tazas tienen un precio de $6750 y los termos de $8075.
# La carga finaliza con cantidad = 0, y puede haber más de una venta por día
# Se pide:
# a) Ingresar el tipo de producto TZ para tazas y TE para termos.
# b) Ingresar la cantidad vendida según el producto seleccionado.
# c) Realizar una función que calcule el máximo de ventas en cantidad para un
# producto dado y mostrar el monto correspondiente.
# d) Calcular el promedio semanal vendido en cantidad.
# e) Validar los datos de entrada, no permitir cantidades negativas

def cargar(tazas, termos):
    for i in range(1,8):
        print(f"Seleccione TZ para tazas y TE para termos - dia {i}")
        tipo = input(f"Ingrese el tipo de producto - dia {i}: ")
        while tipo == "" or (tipo.upper() != "TZ" and tipo.upper() != "TE") :
            print("Error - Los tipos deben ser TZ para tazas o TE para termos")
            tipo = input("Ingrese el tipo de producto: ")
        
        cantidad = int(input(f"Ingrese la cantidad de {tipo.upper()} vendida en día {i}: "))
        while cantidad < 0:
            print("La cantidad no puede ser negativa")
            cantidad = int(input(f"Ingrese la cantidad de {tipo.upper()} vendida en día {i}: "))
        
        while cantidad != 0:
            
            if tipo.upper() == "TZ":
                tazas.append(cantidad)
            else:
                termos.append(cantidad)
            
            print(f"Seleccione TZ para tazas y TE para termos - dia {i}")
            tipo = input(f"Ingrese el tipo de producto - dia {i}: ")
            while tipo == "" or (tipo.upper() != "TZ" and tipo.upper() != "TE") :
                print("Error - Los tipos deben ser TZ para tazas o TE para termos")
                tipo = input("Ingrese el tipo de producto: ")
        
            cantidad = int(input(f"Ingrese la cantidad de {tipo.upper()} vendida en día {i}: "))
            while cantidad < 0:
                print("La cantidad no puede ser negativa")
                cantidad = int(input(f"Ingrese la cantidad de {tipo.upper()} vendida en día {i}: "))
            
def maximo_ventas(producto):
    max = producto[0]
    for i in range(1, len(producto)):
        if producto[i] > max:
            max = producto[i]
    return max

def cantidad_ventas(producto):
    cantidad = 0
    for i in range(len(producto)):
        cantidad += producto[i]
    return cantidad
    
tazas = []
termos = []
cargar(tazas, termos)
if len(tazas) == 0 and len(termos) == 0:
    print("No hay datos para mostrar")
else:
    max_tazas = maximo_ventas(tazas)
    print(f"Máximo tazas {max_tazas} - total ${max_tazas * 6750}")
    max_termos = maximo_ventas(termos)
    print(f"Máximo termos {max_termos} - total ${max_termos * 8075}")
    cantidad_ventas_tazas = cantidad_ventas(tazas)
    cantidad_ventas_termos = cantidad_ventas(termos)
    promedio_semanal = (cantidad_ventas_tazas + cantidad_ventas_termos) / 7
    print(f"El promedio de ventas semanales es de {promedio_semanal}")
    
    
    
    