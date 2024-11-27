def cargar(arr):
    cont = 0
    
    while len(arr) != 6:
        num = int(input("cargar numero: "))
        
        if num % 2 == 0 and num % 7 == 0 and cont < 3:
            arr.append(num)
            cont += 1
        elif num % 2 == 1 and num % 3 == 0 and cont > 3:
            arr.append(num)
            
arr = []
cargar(arr)