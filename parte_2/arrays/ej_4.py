# 4)  Dado un arreglo, imprimir los valores máximo y mínimo.

array_size = int(input("ingresa el tamaño del arreglo: "))
arr = []

value = int(input("ingresa un valor: "))
arr.append(value)
min_value = value
max_value = value

for i in range(1, array_size):
    newValue = int(input("ingresa un valor: "))
    arr.append(newValue)
    if newValue > max_value:
        max_value = newValue
    if newValue < min_value:
        min_value = newValue

print(f"El valor máximo es: {max_value}")
print(f"El valor mínimo es: {min_value}")
