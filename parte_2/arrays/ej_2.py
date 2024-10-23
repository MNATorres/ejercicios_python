# 2) Ingresar un arreglo de 10 componentes:
# a. Imprimir la cuarta componente.
# b. Imprimir las componentes en orden invertida.
# c. Imprimir el producto entre la primera y la última componente.
# d. Imprimir las componentes de índice impar.
# e. Imprimir la suma de las componentes de índice par.
# f. Imprimir la multiplicación de las componentes de índice impar.
# g. Imprimir el arreglo que resulta de intercambiar la primera con la última 
# componente.

arr = []

for i in range(0, 10):
    arr.append(int(input("ingresa el componente: ")))

producto_primero_ultimo = arr[0] * arr [9]
componetes_indice_impar = []
suma_componetes_pares = 0
cont_impares = 0
mult_componentes_impares = 1

for i in range(0,10):
    if i % 2 == 1:
        componetes_indice_impar.append(arr[i])
        cont_impares += 1
    else:
        suma_componetes_pares += arr[i]

for i in range(0, cont_impares):
    mult_componentes_impares *= componetes_indice_impar[i]

print(f"La cuarta de componente es {arr[3]}")
arr.reverse()
print(f"Los componentes invertidos son: {arr}")
arr.reverse()
print(f"El producto entre {arr[0]} y {arr[9]} es {producto_primero_ultimo}") 
print(f"Los componentes de indice impar: {componetes_indice_impar}")
print(f"La suma de componentes pares es {suma_componetes_pares}")

aux = arr[9]
arr[9] = arr[0]
arr[0] = aux
print(f"El arr con intercambiados es: {arr}")



   