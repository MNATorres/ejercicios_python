# En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio: 
# Dos números son amigos si cada uno de ellos es igual a la suma de los divisores del otro.
# Por ejemplo, 220 y 284 son amigos ya que:
# La suma de divisores de 284 es 1 + 2 + 4 + 71 + 142 = 220
# La suma de divisores de 220 es:
# 1 + 2 + 4 + 5 + 10 + 11 + 20 +22 + 44 + 55 + 110 = 284
# Construir un algoritmo usando funciones y luego codificarlo en Python para que dados dos números determine si son amigos.

def resultAdd(num):
    result = 0
    for i in range (1, num):
        if num % i == 0:
            result += i
    return result

def numberFriends(num1, num2):
    if num1 == 0 or num2 == 0:
        print("Los parametros no pueden ser 0")
        return
    dividersNum1 = resultAdd(num1)
    dividersNum2 = resultAdd(num2)
    if dividersNum1 == num2 and dividersNum2 == num1:
        print(f"La suma de los divisores del {num1} es {dividersNum1}")
        print(f"La suma de los divisores del {num2} es {dividersNum2}")
        print("Por lo tanto son numero amigos")
    else :
        print("No son numeros amigos")

numero1 = int(input("ingrese el numero 1 "))
numero2 = int(input("ingrese el numero 2 "))

numberFriends(numero1, numero2)