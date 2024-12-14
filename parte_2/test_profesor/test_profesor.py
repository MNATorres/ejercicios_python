def cargar(vec_facturas, vec_importes, vec_alimentos):
    print("Los alimentos pueden ser para pez, Gato y Perro")
    alimento = input("Ingrese el tipo de alimentos: ").upper()
    while alimento != "PEZ" and alimento != "Gato" and alimento != "PERRO" and alimento != "FIN":
        print("error - Los alimentos pueden ser para Pez, Gato y Perro")
        alimento = input("Ingrese el tipo de alimentos: ").upper()

    while alimento != "FIN":
        
        nr_factura  = int(input("Ingrese numero de factura: "))
        if nr_factura < 0:
            print("error - El número de factura no debe ser negativo")
            
def eliminar(facturas, importes, alimentos):
    for i in range(len(facturas) -1, 0 - 1, -1):
        if facturas[i] % 2 == 1:
            facturas.remove(facturas[i])    
            importes.remove(facturas[i])    
            alimentos.remove(facturas[i])    

def mostar(facturas, importes, alimentos):
    print("Mostrar")