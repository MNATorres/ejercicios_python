# Desarrollar un programa solo con los conceptos vistos hasta el momento para el siguiente ejercicio, codificarlo en lenguaje Python:

#  Se ingresa el nombre y apellido, el saldo de la caja de ahorro y el saldo de la caja de cuenta corriente de los clientes de un banco hasta que el nombre y apellido sea FIN. Calcular y mostrar:

# Nombre y apellido del cliente que tiene el mayor saldo en la caja de ahorro
# Cantidad de clientes cuyo saldo en caja de ahorro o en cuenta corriente sea negativo.
# Total de dinero depositado en ambas cajas.
# Mostrar el nombre y apellido de aquellos clientes que no tienen dinero en ambas cuentas.



def cargar(nombres, apellidos, saldo_ca, saldo_cc):
    nombre = input("Ingrese el nombre: ")
    while nombre == "":
        nombre = input("El nombre no puede estar vacio - Ingrese el nombre: ")
        
    apellido = input("ingrese el apellido: ")
    while nombre == "":
        nombre = input("El apellido no puede estar vacio - Ingrese el apellido: ")
        
    while nombre.upper() != "FIN" and apellido.upper() != "FIN":
        saldo_caja_a = float(input("ingrese saldo de caja de ahorro: "))
        saldo_cuenta_c = float(input("ingrese saldo de cuenta corriente: "))
        
        nombres.append(nombre)
        apellidos.append(apellido)
        saldo_ca.append(saldo_caja_a)
        saldo_cc.append(saldo_cuenta_c)
        
        nombre = input("Ingrese el nombre: ")
        while nombre == "":
            nombre = input("El nombre no puede estar vacio - Ingrese el nombre: ")
        
        apellido = input("ingrese el apellido: ")
        while nombre == "":
            nombre = input("El apellido no puede estar vacio - Ingrese el apellido: ")
        
def mayor_saldo_cc(saldo_cc):
    ind_aux = 0
    for i in range(len(saldo_cc)):
        if saldo_cc[i] > saldo_cc[ind_aux]:
            ind_aux = i
    return ind_aux

def saldos_negativos(caja_ahorro, cuenta_corriente):
    count = 0
    for i in range(len(caja_ahorro)):
        if caja_ahorro[i] < 0 or cuenta_corriente[i] < 0:
            count += 1
    return count

def suma_dinero(cuenta):
    acumulador = 0
    for i in range(len(cuenta)):
        acumulador += cuenta[i]
    return acumulador

def usuarios_sin_dinero(nombres, apellidos, caja_ahorro, cuenta_corriente):
    for i in range(len(nombres)):
        if caja_ahorro[i] < 1 and cuenta_corriente[i] < 1:
            print(f"El usuario {nombres[i]} {apellidos[i]} no tiene dinero en ambas cuentas")
    

nombres = ["Carlos", "María", "José", "Ana", "Luis"]
apellidos = ["Gómez", "Fernández", "Pérez", "Martínez", "Rodríguez"]
caja_ahorro = [1500.75, -234.60, 980.00, 3200.20, -120.50]
cuenta_corriente = [200.00, -1350.40, -75.25, -450.60, -980.15]
# cargar(nombres, apellidos, caja_ahorro, cuenta_corriente)
print(f"nombres: {nombres}")
print(f"apellidos: {apellidos}")
print(f"saldo_ca: {caja_ahorro}")
print(f"saldo_cc: {cuenta_corriente}")
if len(nombres) > 0:
    max_saldo_ca = mayor_saldo_cc(caja_ahorro)
    print(f"El usuario {nombres[max_saldo_ca]} {apellidos[max_saldo_ca]} tiene mayor saldo en caja de ahorro ${caja_ahorro[max_saldo_ca]}")
    cont_saldos_negativos = saldos_negativos(caja_ahorro, cuenta_corriente)
    print(f"Hay un total de {cont_saldos_negativos} clientes con saldos negativos")
    dinero_ca = suma_dinero(caja_ahorro)
    dinero_cc = suma_dinero(cuenta_corriente)
    print(f"Dinero en ca {dinero_ca}")
    print(f"Dinero en cc {dinero_cc}")
    usuarios_sin_dinero(nombres, apellidos, caja_ahorro, cuenta_corriente)
    
    
    