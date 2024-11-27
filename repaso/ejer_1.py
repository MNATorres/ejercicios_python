CAPACIDAD_SALA_A = 50

total_entradas = 0
total_la_sirenita = 0
total_mario = 0
total_entradas_pochoclo = 0
total_sala_a = 0

cant_entradas = int(input("ingrese la cantidad de entradas: "))
while cant_entradas < 0:
    cant_entradas = int(input("error - ingrese la cantidad de entradas: "))

while cant_entradas != 0:
    total_entradas += cant_entradas
    
    sala = input("Ingrese la sala A/B: ")
    while sala.upper() != 'A' and sala.upper() != 'B':
        print("Las opciones disponibles son A o B")
        sala = input("Ingrese la sala A/B: ")
    if sala.upper() == 'A':
        total_sala_a += cant_entradas
    
    print("Las peliculas disponibles son La Sirenita y Super Mario Bros")
    pelicula = input("ingrese nombre de la pelicula: ")
    while pelicula.upper() != 'LA SIRENITA' and pelicula.upper() != 'SUPER MARIO BROS':
        print("La pelicula es incorrecta - Las peliculas disponibles son La Sirenita y Super Mario Bros")
        pelicula = input("ingrese nombre de la pelicula: ")
    if pelicula.upper() == 'LA SIRENITA':
        total_la_sirenita += cant_entradas
    else:
        total_mario += cant_entradas

    
    pochoclos = input("lleva pochoclos? si/no: ")
    while pochoclos.upper() != 'SI' and pochoclos.upper() != 'NO':
        print("las opciones son Si o No")
        pochoclos = input("lleva pochoclos? si/no: ")
    if pochoclos.upper() == 'SI':
        total_entradas_pochoclo += cant_entradas
        
    cant_entradas = int(input("ingrese la cantidad de entradas: "))
    while cant_entradas < 0:
        cant_entradas = int(input("error - ingrese la cantidad de entradas: "))

if total_entradas > 0:
    print(f"El porcentaje de entradas con pochoclo es {(total_entradas_pochoclo/total_entradas) * 100}%")
    
    if total_la_sirenita > total_mario:
        print(f"Se vendieron mas entras para La Sirenita, un total de {total_la_sirenita}")
    elif total_mario > total_la_sirenita:
        print(f"Se vendieron mas entras para Super Mario Bros, un total de {total_mario}")
    else:
        print("Se vendieron las mismas entradas para ambos")
    
    ocup_sala_a = (total_sala_a / CAPACIDAD_SALA_A) * 100
    if ocup_sala_a > 50:
        print("Se ocupó mas del %50 de la capacidad de la sala A")
else:
    print("no se vendieron entradas")
    

    



