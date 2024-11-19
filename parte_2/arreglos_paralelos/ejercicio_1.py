# Se pide guardar los nombres y los sueldos de los empleados de un sector. La carga
# finaliza cuando se lee FIN en el nombre del empleado. Se quiere determinar el
# nombre del empleado que tiene el sueldo más grande. 

def cargarSueldoYNombres(nombres, sueldos):
    nombre = input("ingrese el nombre: ").upper()
    while nombre == '' or nombre.isspace():
        nombre = input("Nombre invalido, ingrese el nombre: ").upper()
        
    while nombre != "FIN":
        sueldo = float(input("ingrese el sueldo: "))
        while sueldo <= 0:
            sueldo = float(input("Sueldo invalido, ingrese el sueldo: "))
    
        nombres.append(nombre)
        sueldos.append(sueldo)
        nombre = input("ingrese el nombre: ").upper()
        while nombre == '' or nombre.isspace():
            nombre = input("Nombre invalido, ingrese el nombre: ").upper()

def mostrarNombreYSueldos(nombres, sueldos):
    for i in range(len(nombres)):
        print(f"El nombre es {nombres[i]} y su sueldo es {sueldos[i]}")
        
def indiceSueldoMasBajo(sueldos):
    index = 0
    for i in range(len(sueldos)):
        if sueldos[i] < sueldos[index]:
            index = i
    return index

nombres = []
sueldos = []
cargarSueldoYNombres(nombres, sueldos)
mostrarNombreYSueldos(nombres, sueldos)
indiceAuxiliar = indiceSueldoMasBajo(sueldos)
print(f"El sueldo mas bajo es de {nombres[indiceAuxiliar]} con un sueldo {sueldos[indiceAuxiliar]}")
