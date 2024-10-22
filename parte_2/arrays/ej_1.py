# Ingresar un arreglo e imprimirlo. Se da como dato el número de componentes del 
# vector.

data = int(input("ingrese la cantidad de elementos: "))
arr = []

for i in range(0, data):
    arr.append(int(input("ingrese un valor: ")))

for i in range(0, data):
    print(arr[i])

print(f"el numero de componentes del vector es  {data}")