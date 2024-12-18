def mostrar(nombre, apellido, edad):
    print("---datos---")
    for i in range(len(nombre)):
        print(f"nombre: {nombre[i]} | apellido: {apellido[i]} | edad: {edad[i]}")
        

def ordenar(vec1, vec2, vec3):
    for i in range(0, len(nombre) - 1, 1):
        for j in range(i + 1, len(nombre), 1):
            if vec1[i] > vec1[j]:
                cambiar_orden(vec1, i, j)
                cambiar_orden(vec2, i, j)
                cambiar_orden(vec3, i, j)
                
def cambiar_orden(vec, i, j):
    aux = vec[i]
    vec[i] = vec[j]
    vec[j] = aux
    
def eliminar(nombre, apellido, edad):
    for i in range(len(nombre) - 1, -1, -1):
        if(edad[i] % 2 == 1):
            edad.pop(i)
            apellido.pop(i)
            nombre.pop(i)
            
        

nombre = ["Ana", "Carlos", "Luisa", "Miguel", "Sofía"]
apellido = ["Gómez", "Pérez", "Martínez", "Rodríguez", "López"]
edad = [25, 30, 28, 35, 22]
if len(nombre) > 0:
    mostrar(nombre, apellido, edad)
    ordenar(edad, nombre, apellido)
    mostrar(nombre, apellido, edad)
    eliminar(nombre, apellido, edad)
    mostrar(nombre, apellido, edad)
else:
    print("No hay datos disponibles")

