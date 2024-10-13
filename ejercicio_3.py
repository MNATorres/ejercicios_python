# 3. Una cerealera desea clasificar sus clientes de acuerdo con las toneladas que le
# compran.
# • Cliente que compra menos de 100 toneladas: chico.
# • Cliente que compra entre 100 y 300 toneladas: mediano.
# • Cliente que compra más de 300 toneladas: grande.
# Se desea diseñar un algoritmo que permita el ingreso de las toneladas por cliente y
# el tipo de cliente (chico, mediano o grande). Finaliza el ingreso de datos cuando se
# ingrese las toneladas igual a 000. Luego muestre la siguiente información por
# pantalla:
# a) Cantidad de clientes.
# b) Calcular el valor total de toneladas vendidas, sabiendo que la tonelada cuesta
# 250 dólares, y que los clientes grandes tienen un descuento del 5%.
# c) Porcentaje de toneladas vendidas por categoría. (cantidad_categoria*100/Total)

cantidad_clientes = 0
total_ventas = 0
cantidad_toneladas = 0
toneladas_chico = 0
toneladas_mediano = 0
toneladas_grande = 0

toneladas = int(input("ingrese cantidad de toneladas: "))
while toneladas < 0:
    print("no se permiten nnumeros negativos")
    toneladas = int(input("ingrese cantidad de toneladas: "))

while toneladas != 0:
    cantidad_clientes += 1
    cantidad_toneladas += toneladas
    
    if toneladas < 100:
        total_ventas += toneladas * 250
        toneladas_chico += toneladas
    elif 100 <= toneladas <= 300:
        total_ventas += toneladas * 250
        toneladas_mediano += toneladas
    else:
        total_ventas += (toneladas * 250) * 0.95
        toneladas_grande += toneladas
        
    toneladas = int(input("ingrese cantidad de toneladas: "))
    while toneladas < 0:
        print("no se permiten nnumeros negativos")
        toneladas = int(input("ingrese cantidad de toneladas: "))

if cantidad_clientes == 0:
    print("no hay datos para mostrar")
else:
    print(f"Hay una cantidad de {cantidad_clientes} de clientes.")
    print(f"Se vendió un total de {total_ventas}")
    print(f"procentaje de ventas chico {(toneladas_chico * 100) / cantidad_toneladas}")
    print(f"procentaje de ventas mediano {(toneladas_mediano * 100) / cantidad_toneladas}")
    print(f"procentaje de ventas grande {(toneladas_grande * 100) / cantidad_toneladas}")
    