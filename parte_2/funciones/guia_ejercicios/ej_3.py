# 3. Diseñar una función que calcule el triple de un número y otra función que calcule el 
# siguiente de un número. Utilizar las funciones en un programa para que ingresado un 
# numero muestre el consecutivo del triple del número y el triple del consecutivo del 
# número.

def calculateTriple(numb):
    return numb * 3

def calculateNextNumber(numb):
    return numb + 1

def calculateTripleAndNext(numb):
    triple = calculateTriple(numb)
    nextNumber = calculateNextNumber(triple)
    print(f"El consecutivo del triple del numero {numb} es {nextNumber}")
    
    nextNumber = calculateNextNumber(numb)
    triple = calculateTriple(nextNumber)
    print(f"El triple del consecutivo de {numb} es {triple}")
    
number = int(input("ingrese un número: "))
calculateTripleAndNext(number)