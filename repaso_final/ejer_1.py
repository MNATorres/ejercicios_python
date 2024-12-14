# Se ingresa el nombre y apellido, el saldo de la caja de ahorro y el saldo de la caja de cuenta corriente de los clientes de un banco hasta que el nombre y apellido sea FIN. Calcular y mostrar:

# Nombre y apellido del cliente que tiene el mayor saldo en la caja de ahorro
# Cantidad de clientes cuyo saldo en caja de ahorro o en cuenta corriente sea negativo.
# Total de dinero depositado en ambas cajas.
# Mostrar el nombre y apellido de aquellos clientes que no tienen dinero en ambas cuentas.

def cargar(nombres, apellidos, caja_ahorro, cuenta_corriente):
    nombre = input('Ingrese el nombre: ')
    while nombre == '':
        nombre = input('Error - Ingrese el nombre: ')
    
    apellido = input('Ingrese el apellido: ')
    while apellido == '':
        apellido = input('Error - Ingrese el apellido: ')
    
    while not(nombre.upper() == 'FIN' and apellido.upper() == 'FIN'):
        saldoca = float(input('Ingrese el saldo de la caja de ahorro: '))
            
        saldocc = float(input('Ingrese el saldo de cuenta corriente: '))
        
        nombres.append(nombre)
        apellidos.append(apellido)
        caja_ahorro.append(saldoca)
        cuenta_corriente.append(saldocc)
        
        nombre = input('Ingrese el nombre: ')
        while nombre == '':
            nombre = input('Error - Ingrese el nombre: ')

    
        apellido = input('Ingrese el apellido: ')
        while apellido == '':
            apellido = input('Error - Ingrese el apellido: ')

def mostrar(nombres, apellidos, caja_ahorro, cuenta_corriente):
    print("Mostrar datos")
    for i in range(len(nombres)):
        print(f"nb: {nombres[i]} | ap: {apellidos[i]} | ca: {caja_ahorro[i]} | cc: {cuenta_corriente[i]}")

def mayor_saldo_ca(caja_ahorro):
    index_aux = 0
    for i in range(len(caja_ahorro)):
        if caja_ahorro[i] > caja_ahorro[index_aux]:
            index_aux = i
    return index_aux

def saldo_negativo(caja_ahorro, cuenta_corriente):
    count = 0
    for i in range(len(caja_ahorro)):
        if caja_ahorro[i] < 0 or cuenta_corriente[i] < 0:
            count += 1
    return count    

def totalSaldo(cuenta):
    total = 0
    for i in range(len(cuenta)):
        total += cuenta[i]
    return total

def clientes_sin_saldo(nombres, apellidos, caja_ahorro, cuenta_corriente):
    for i in range(len(nombres)):
        if caja_ahorro[i] <= 0 and cuenta_corriente[i] <= 0:
            print(f"El cliente {nombres[i]} {apellidos[i]} no tiene dinero en ambas cuentas")
           
nombres = []
apellidos = []
caja_ahorro = []
cuenta_corriente = []

cargar(nombres, apellidos, caja_ahorro, cuenta_corriente)
if len(nombres) > 0:
    mostrar(nombres, apellidos, caja_ahorro, cuenta_corriente)
    iMayorCa = mayor_saldo_ca(caja_ahorro)
    print(f"Cliente con mayor saldo en caja de ahorro: {nombres[iMayorCa]} {apellidos[iMayorCa]} con un saldo de ${caja_ahorro[iMayorCa]},")
    cont_saldo_negativo = saldo_negativo(caja_ahorro, cuenta_corriente)
    print(f"Hay {cont_saldo_negativo} clientes con saldo negativo en ca o cc")
    total_ca = totalSaldo(caja_ahorro)
    total_cc = totalSaldo(cuenta_corriente)
    print(f"En caja de ahorro hay ${total_ca}, cuenta corriente ${total_cc}, y el total de ambas ${total_ca + total_cc}")
    clientes_sin_saldo(nombres, apellidos, caja_ahorro, cuenta_corriente)
else:
    print("No hay datos para mostrar")