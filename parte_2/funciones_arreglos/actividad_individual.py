# En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio: 
# Ingresar números enteros hasta que sea dicho número cero y cargar un arreglo con aquellos números múltiplos de 5. Mostrar el arreglo y calcular:
# a. Los 3 primeros números más grandes.
# b. Generar otro arreglo con los números múltiplos de 10. Si no los hubiera mostrar una leyenda.
# c. Eliminar del arreglo original el valor mínimo. Si los hubiera repetido, eliminar todas las apariciones del elemento mínimo

def ingresarNumeros(arr):
    numero = int(input("ingrese numero: "))
    while numero != 0:
        if(numero % 5 == 0):
            arr.append(numero)
        numero = int(input("ingrese otro numero: "))
    print(f"arreglo: {arr}")
    
def numerosGrandes(arr):
    result = [] * 3
    arr.sort(reverse=True)
    result.append(arr[0])
    result.append(arr[1])
    result.append(arr[2])
    return result

def multDiez(arr):
    if len(arr) == 0: 
        print("No hay datos en la lista")
        return []
    
    result = []
    
    for i in range(len(arr)):
        if arr[i] % 10 == 0:
            result.append(arr[i])
            
    if len(result) == 0:
        print("no hay multiplos de 10")
    else:
        return result
    
def eliminarMinimo(arr):
    if len(arr) == 0: 
        print("No hay datos en la lista")
        return []
    
    result = []
    minimo = arr[len(arr) - 1] # la lista esta ordenada de maor a menor
    
    for i in range(len(arr)):
        if arr[i] != minimo:
            result.append(arr[i])
    return result

array = []
ingresarNumeros(array)
print(f"los 3 numeros mas grandes son {numerosGrandes(array)}")
print(f"los multiplos de 10 son: {multDiez(array)}")
print(f"la lista sin el elemento minimo es {eliminarMinimo(array)}")