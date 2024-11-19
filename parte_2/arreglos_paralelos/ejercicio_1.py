# Se pide guardar los nombres y los sueldos de los empleados de un sector. La carga
# finaliza cuando se lee FIN en el nombre del empleado. Se quiere determinar el
# nombre del empleado que tiene el sueldo más grande. 

def cargarDatos(nombres, sueldos, edades):
    nombre = input("ingrese el nombre: ").upper()
    while nombre == '' or nombre.isspace():
        nombre = input("Nombre invalido, ingrese el nombre: ").upper()
        
    while nombre != "FIN":
        sueldo = float(input("ingrese el sueldo: "))
        while sueldo <= 0:
            sueldo = float(input("Sueldo invalido, ingrese el sueldo: "))
        
        edad = int(input("Ingrese la edad: "))
        while(edad < 1):
            edad = int(input("Error - Ingrese la edad: "))
    
        nombres.append(nombre)
        sueldos.append(sueldo)
        edades.append(edad)
        nombre = input("ingrese el nombre: ").upper()
        while nombre == '' or nombre.isspace():
            nombre = input("Nombre invalido, ingrese el nombre: ").upper()

def mostrarDatos(nombres, sueldos, edades):
    for i in range(len(nombres)):
        print(f"El nombre: {nombres[i]}, sueldo: {sueldos[i]}, edad: {edades[i]}")
        
def indiceSueldoMasBajo(sueldos):
    index = 0
    for i in range(len(sueldos)):
        if sueldos[i] < sueldos[index]:
            index = i
    return index

def cambiarOrden(arr, a, b):
    aux = arr[a]
    arr[a] = arr[b]
    arr[b] = aux

def ordenar(vec_ord, vec2, vec3):
    auxLen = len(vec_ord)
    for i in range(0, auxLen -1, 1):
        for j in range(i + 1, auxLen, 1):
            if vec_ord[i] > vec_ord[j]:
                cambiarOrden(vec_ord, i, j)
                cambiarOrden(vec2, i, j)
                cambiarOrden(vec3, i, j)


nombres = []
sueldos = []
edades = []
cargarDatos(nombres, sueldos, edades)

if len(nombres) > 0:
    mostrarDatos(nombres, sueldos, edades)
    indiceAuxiliar = indiceSueldoMasBajo(sueldos)
    print(f"El sueldo mas bajo es de {nombres[indiceAuxiliar]} con un sueldo {sueldos[indiceAuxiliar]}")
    ordenar(nombres, sueldos, edades)
    mostrarDatos(nombres, sueldos, edades)

