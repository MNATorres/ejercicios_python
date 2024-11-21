def cargar(arr):
    num = int(input("ingrese un nuemero: "))
    while num != 0:
        arr.append(num)
        num = int(input("ingrese un numero: "))

numeros = []
cargar(numeros)
if len(numeros) > 0:
    print(f"Estos so los numeros {numeros}")