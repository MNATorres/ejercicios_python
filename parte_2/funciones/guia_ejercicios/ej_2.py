# 2. Construir una función que permite devolver la potencia de un número ingresando el 
# número y su potencia.

def calculatePower(numb, power):
    if numb == 0 :
        return "El número base no puede ser 0"
    return numb ** power

numb = int(input("ingresa el numero base "))
power = int(input("ingresa la potencia "))
result = calculatePower(numb, power)
print(f"resultado {result}")
