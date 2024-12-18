# Se desea llevar el control de planes de una prepaga para las localidades más
# populares CABA y BSAS, y realizar la estadística mensual. Para ello se releva la
# siguiente información.
# • Localidad
# • Tipo de plan: Oro (O), Plata (P)
# • Cantidad de consultas realizadas
# • Día en que se realizaron las consultas
# Se deberán cargar cuatro arreglos con la información pedida, uno para cada dato.
# Validar los datos de entrada con criterios lógicos. La carga finaliza cuando se ingresa
# día 0. Se pide:
# a) Mostrar los datos cargados.
# b) Realizar una función que calcule el día de más consultas y luego mostrar a
# qué zona y plan corresponde.
# c) Realizar una función que, dado un día, determine en cuál de los dos planes
# tuvo menos consultas.
# d) Calcular el promedio de consultas realizadas en el mes.

def cargar(dias_mes, localidades, planes, cantidad_consultas):
    for i in range(1,31):
        cantidad_consultas.append([[],[]])
        planes.append([[],[]])
    
    dia = int(input("Ingrese el día: "))
    while dia < 0 or dia > 31:
        dia = int(input("Día incorrecto - Ingrese el día: "))
    
    while dia != 0:
        print("Localidades disponibles CABA y BSAS")
        localidad = input("Ingrese la localidad: ")
        while localidad.upper() != "CABA" and localidad.upper() != "BSAS":
            print("error - Localidades disponibles CABA y BSAS")
            localidad = input("Ingrese la localidad: ")
        
        print("Planes disponibles Oro (O), Plata (P)")
        plan = input("Ingrese tipo de plan: ")
        while plan.upper() != "O" and plan.upper() != "P":
            print("error - Planes disponibles Oro (O), Plata (P)")
            plan = input("Ingrese tipo de plan: ")
        
        consultas = int(input("Ingrese la cantidad de consultas: "))
        while consultas < 0:
            print("Error - Las consultas no deben ser un número negativo")
            consultas = int(input("Ingrese la cantidad de consultas: "))
         
        dias_mes.append(dia)
        localidades.append(localidad)
        
        if plan.upper() == "P":
            cantidad_consultas[dia][0].append(cantidad_consultas)
            planes[dia][0].append(plan)   
        else:
            cantidad_consultas[dia][1].append(cantidad_consultas)
            planes[dia][1].append(plan)
            
        dia = int(input("Ingrese el día: "))
        while dia < 0 or dia > 31:
            dia = int(input("Día incorrecto - Ingrese el día: "))
        
def mostrar(dias_mes,localidades, planes, cantidad_consultas):
    print("Mostrar datos")
    for i in range(len(dias_mes)):
        print(f"dias del mes {dias_mes[i]}")
        print(f"localidades {localidades[i]}")
        print(f"plan plata: {planes[i][0]}, plan oro: {planes[i][1]}")
        print(f"cantidad_consultas plan plata {cantidad_consultas[i][0]}, plan oro: {cantidad_consultas[i][1]}")
        

dias_mes = []
localidades = [] 
planes = []
cantidad_consultas = []
cargar(dias_mes,localidades, planes, cantidad_consultas)
mostrar(dias_mes,localidades, planes, cantidad_consultas)