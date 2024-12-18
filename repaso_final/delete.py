Vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(Vector) - 1, -1, -1):  # Recorrer de atrás hacia adelante
    if Vector[i] % 2 != 0:  # Si el número es impar
        Vector.pop(i)

print(Vector)  # Salida: [2, 4, 6, 8, 10]