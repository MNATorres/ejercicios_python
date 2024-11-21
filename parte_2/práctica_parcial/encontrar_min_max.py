def cargar(pares, impares):
    num = int(input("Ingrese un número: "))
    while num != 0:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        num = int(input("ingrese un numero: "))

def minimo(arreglo):
    index = 0
    for i in range(len(arreglo)):
        if arreglo[i] < arreglo[index]:
            index = i
    return index

def maximo(arreglo):
    index = 0
    for i in range(len(arreglo)):
        if arreglo[i] > arreglo[index]:
            index = i
    return index

def intercambio(pares, impares, min, max):
    aux = pares[min]
    pares[min] = impares[max]
    impares[max] = aux

pares = []
impares = []
cargar(pares, impares)
print(f"numeros pares {pares}")
print(f"numeros pares {impares}")
min = minimo(pares)
max = maximo(impares)
print(f"El numero minimo es {pares[min]}")
print(f"El maximo es {impares[max]}")
intercambio(pares, impares, min, max)
print(f"pares {pares}")
print(f"impares {impares}")