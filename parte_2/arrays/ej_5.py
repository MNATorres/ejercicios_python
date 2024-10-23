# 5) Dado un arreglo, imprimir el lugar que ocupa el mínimo. Tener en cuenta que este valor 
# puede estar repetido, en ese caso imprimir todos los lugares donde aparece este valor.

arr = [5, 3, 1, 7, 2, 1, 8, 9, 1, 4, 6, 0, 3, 7, 0, 2, 5, 0]

min_value = arr[0]
positions = []

for i in range(len(arr)):
    if arr[i] < min_value:
        min_value = arr[i]
        positions = [i]
    elif arr[i] == min_value:
        positions.append(i)

print(f"El valor mínimo es {min_value} y sus index son {positions}")


