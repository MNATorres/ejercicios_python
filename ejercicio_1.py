CAPACIDAD_A = 50

acumulador_con_pochoclo = 0
acumulador_la_sirenita = 0
acumulador_super_mario = 0
acumulador_sala_a = 0
acumulador_entradas = 0

cantidad_entradas = int(input("ingrese cantidad de entradas: "))
while cantidad_entradas < 0:
    print("las entradas no pueden ser un número negativo")
    cantidad_entradas = int(input("ingrese cantidad de entradas: "))
    
while cantidad_entradas != 0:
    acumulador_entradas += cantidad_entradas
    
    letra_sala = input("ingrese letra de sala(A/B): ")
    while letra_sala.upper() != "A" and letra_sala.upper() != "B":
        print("la sala debe ser A o B")
        letra_sala = input("ingrese letra de sala(A/B): ")
    if letra_sala.upper() == 'A':
        acumulador_sala_a += cantidad_entradas
    
    print("Peliculas disponibles: La Sirenita / Super Mario Bros")    
    nombre_pelicula = input("ingrese nombre de pelicula: ")
    while nombre_pelicula.upper() != "LA SIRENITA" and nombre_pelicula.upper() != "SUPER MARIO BROS":
        print("Peliculas disponibles: La Sirenita / Super Mario Bros")    
        nombre_pelicula = input("ingrese nombre de pelicula: ")
    if nombre_pelicula.upper() == "LA SIRENITA":
        acumulador_la_sirenita += cantidad_entradas
    else:
        acumulador_super_mario += cantidad_entradas
    
    lleva_pochoclos = input("lleva pochoclos (si/no)?")
    while lleva_pochoclos.upper() != "SI" and lleva_pochoclos.upper() != "NO":
        print("los vaalores de lleva pochoclos debe ser si/no")
        lleva_pochoclos = input("lleva pochoclos (si/no)?")
    if lleva_pochoclos.upper() == "SI":
        acumulador_con_pochoclo += cantidad_entradas
    
    cantidad_entradas = int(input("ingrese cantidad de entradas: "))
    while cantidad_entradas < 0:
        print("las entradas no pueden ser un número negativo")
        cantidad_entradas = int(input("ingrese cantidad de entradas: "))

print(f"El porcentaje de entradas con pochoclo es de: {(acumulador_con_pochoclo / acumulador_entradas) * 100}")

if acumulador_la_sirenita > acumulador_super_mario:
    print(f"Se vendieron mas entradas de La sirenita, total {acumulador_la_sirenita}")
else:
    print(f"se vendieron mas entradas de Super Mario, total: {acumulador_super_mario}")
    
if acumulador_sala_a > CAPACIDAD_A/2:
    print(f"Se superó mas del %50 de ocupación. Total {acumulador_sala_a} espectadores")    
    
    