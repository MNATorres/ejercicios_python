# 1. Construir una función que permita devolver el valor absoluto de un número ingresado 
# por teclado.

def absoluteValue(numb):
    if numb < 0:
        return numb * -1
    else: 
        return numb

numb = float(input("ingrese un numero: "))
result = absoluteValue(numb)
print(result)