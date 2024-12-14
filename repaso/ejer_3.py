# . Una cerealera desea clasificar sus clientes de acuerdo con las toneladas que le
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

PRECIO_TONELADA = 250

cont_clientes = 0
total_vendido = 0
toneladas_chico = 0
toneladas_mediano = 0
toneladas_grande = 0
precio_descuento = PRECIO_TONELADA * (1 - (5 / 100))

while True:
    toneladas = int(input("Ingrese la cantidad de toneladas (0 para finalizar): "))
    while toneladas < 0:
        toneladas = int(input("Error - Ingrese un valor positivo para las toneladas: "))

    if toneladas == 0:  # Condición de salida
        break

    cont_clientes += 1

    if toneladas < 100:
        total_vendido += toneladas * PRECIO_TONELADA
        toneladas_chico += toneladas
    elif 100 <= toneladas <= 300:
        total_vendido += toneladas * PRECIO_TONELADA
        toneladas_mediano += toneladas
    else:
        total_vendido += toneladas * precio_descuento
        toneladas_grande += toneladas

# Mostrar resultados
print(f"\nLa cantidad de clientes es: {cont_clientes}")
print(f"El total vendido es: ${total_vendido:.2f}")

# Calcular porcentaje por categoría
total_toneladas = toneladas_chico + toneladas_mediano + toneladas_grande
if total_toneladas > 0:
    porcentaje_chico = (toneladas_chico * 100) / total_toneladas
    porcentaje_mediano = (toneladas_mediano * 100) / total_toneladas
    porcentaje_grande = (toneladas_grande * 100) / total_toneladas

    print(f"El porcentaje de ventas de cliente chico es: {porcentaje_chico:.2f}%")
    print(f"El porcentaje de ventas de cliente mediano es: {porcentaje_mediano:.2f}%")
    print(f"El porcentaje de ventas de cliente grande es: {porcentaje_grande:.2f}%")
else:
    print("No se vendieron toneladas en ninguna categoría.")
