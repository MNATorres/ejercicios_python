# 2. En un reconocido banco de la Ciudad de Buenos Aires, los clientes se han formado
# en una cola por orden de llegada. Con el objeto de llevar registros sobre los clientes
# que van a la entidad bancaria, el gerente necesita realizar ciertos cálculos sobre las
# edades de estos. En el banco hay 3 tipos de clientes numerados del 1 al 3 según el
# tipo de cuenta que poseen. De cada cliente se conoce la siguiente información:
# • Nombre del cliente
# • Edad (valor entero)
# • Tipo_de_cliente (valor entero de 1 a 3)
# Para simplificar su trabajo, el gerente te pide que desarrolles una aplicación, que
# obtenga los siguientes resultados:
# a) La cantidad de clientes por cada tipo de cuenta.
# b) La edad del cliente más joven (se supone único).
# c) El promedio de las edades, considerando solo a los clientes del tipo 3.
# • Se ingresan datos de clientes hasta que el tipo de cuenta sea cero.

clientes_cuenta_1 = 0
clientes_cuenta_2 = 0
clientes_cuenta_3 = 0
acumulador_edades_cuenta_3 = 0
cliente_joven = 999

tipo_cuenta = int(input("ingrese tipo de cuenta (1,2 o 3): "))
while not(0 <= tipo_cuenta <= 3):
    print("la cuenta debe ser 1,2 o 3")
    tipo_cuenta = int(input("ingrese tipo de cuenta: "))

while tipo_cuenta != 0:
    
    edad = int(input("ingrese la edad: "))
    while edad < 1:
        print("la edad debe ser mayor a 1")
        edad = int(input("ingrese la edad: "))
    if edad < cliente_joven:
        cliente_joven = edad
    
    if tipo_cuenta == 1:
        clientes_cuenta_1 += 1
    elif tipo_cuenta == 2:
        clientes_cuenta_2 += 1
    else:
        clientes_cuenta_3 += 1
        acumulador_edades_cuenta_3 += edad
    
    tipo_cuenta = int(input("ingrese tipo de cuenta (1,2 o 3): "))
    while not(0 <= tipo_cuenta <= 3):
        print("la cuenta debe ser 1,2 o 3")
        tipo_cuenta = int(input("ingrese tipo de cuenta: "))

if tipo_cuenta == 0 and cliente_joven == 999:
    print("no hay datos disponibles")
else: 
    print("Hay un total de %d clinetes de tipo 1, %d de tipo 2 y %d de tipo 3" %(clientes_cuenta_1, clientes_cuenta_2, clientes_cuenta_3))
    print(f"el cliente mas joven es de {cliente_joven}")
    if clientes_cuenta_3 > 0:
        print(f"el promedio de las edades de cuenta 3 es de {acumulador_edades_cuenta_3/clientes_cuenta_3}")
    else:
        print("no hay clientes de cuenta 3")