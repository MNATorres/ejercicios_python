def cargar(arr):
    num = int(input("ingrese un nuemero: "))
    while num != 0:
        arr.append(num)
        num = int(input("ingrese un numero: "))

def eliminar_pares(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr.pop(arr[i])

numeros = []
cargar(numeros)
if len(numeros) > 0:
    print(f"Estos so los numeros {numeros}")
    eliminar_pares(numeros)
    print(f"estos son los impares {numeros}")