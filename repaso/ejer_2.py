# . En un reconocido banco de la Ciudad de Buenos Aires, los clientes se han formado
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

cant_cliente_1 = 0
cant_cliente_2 = 0
cant_cliente_3 = 0
acu_edades_cliente_3 = 0
cliente_mas_joven = 9999

tipo_cliente = int(input("Ingrese tipo de cuenta: "))
while tipo_cliente < 0 or tipo_cliente > 3:
    print("El tipo de cuenta solo debe ser 1,2 o 3")
    tipo_cliente = int(input("Ingrese tipo de cuenta: "))

while tipo_cliente != 0:
    
    nombre = input("ingrese el nombre: ")
    if nombre == '':
        nombre = input("error - ingrese el nombre: ")
    
    edad = int(input("Ingrese la edad: "))
    if edad < 0:
        edad = int(input("error - Ingrese la edad: "))
    if edad < cliente_mas_joven:
        cliente_mas_joven = edad
        
    if tipo_cliente == 1:
        cant_cliente_1 += 1
    elif tipo_cliente == 2:
        cant_cliente_2 += 1
    else:
        cant_cliente_3 += 1
        acu_edades_cliente_3 += edad
    
    tipo_cliente = int(input("Ingrese tipo de cuenta: "))
    while tipo_cliente < 0 or tipo_cliente > 3:
        print("El tipo de cuenta solo debe ser 1,2 o 3")
        tipo_cliente = int(input("Ingrese tipo de cuenta: "))

print(f"Cantidad de clientes cuenta 1 = {cant_cliente_1}")
print(f"Cantidad de clientes cuenta 2 = {cant_cliente_2}")
print(f"Cantidad de clientes cuenta 3 = {cant_cliente_3}")
print(f"El cliente mas joven tiene {cliente_mas_joven} años de edad")
if cant_cliente_3 > 0:
    print(f"El promedio de las edades del cliente tipo 3 es {acu_edades_cliente_3 / cant_cliente_3}")
else:
    print("No hay clientes del tipo 3")    