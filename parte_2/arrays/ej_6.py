# 6. Se pide cargar en memoria un arreglo de N posiciones. Se pide generar un programa 
# que emita un ranking con los 10 números más grandes.

arr = [45, 22, 67, 89, 12, 78, 33, 56, 98, 10, 5, 34, 71, 88, 49, 55, 23, 99, 66, 18]
result = []
arr.sort(reverse=True)

for i in range(0,9):
    result.append(arr[i])

# otra forma
resultOtro = arr[:10]

print(result, resultOtro)