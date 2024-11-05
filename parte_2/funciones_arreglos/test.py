# Definir una función que sume las componentes de un arreglo y devuelva las suma al
# programa principal

def suma(arr):
    suma = 0
    for i in range(len(arr)):
        print(arr[i])
        suma += arr[i]
    return suma
        

arr = [1,2,3,4,5,6,7,8,9,10]
result = suma(arr)
print(f"el resultado es, {result}")