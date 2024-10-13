# Guía de ejercicios de integración en Python

1. El cine Atlas de Flores decide digitalizar el control de ventas de entradas para las
películas infantiles que estarán en cartelera durante las vacaciones de invierno. Las
películas en cartel son: “La Sirenita” y “Super Mario Bros“. Para la venta de las
entradas se pide al usuario que ingrese la siguiente información:
- Cantidad de entradas (valor entero)
- Letra de sala (valor char A o B)
- Nombre de película (cadena de caracteres)
- Lleva pochoclos (si o no)
a) Calcular el porcentaje de ventas de entradas que incluyen pochoclos sobre el
total de entradas.
b) Determinar la película para la que se vendieron más entradas.
c) La sala A tiene una capacidad de 50 personas, mostrar una leyenda en el caso
que se supere el 50% de ocupación.
- Validar el ingreso correcto de la letra de la sala (solo A o B).
- La carga finaliza cuando en cantidad de entradas se ingrese un 0.
  
2. En un reconocido banco de la Ciudad de Buenos Aires, los clientes se han formado
en una cola por orden de llegada. Con el objeto de llevar registros sobre los clientes
que van a la entidad bancaria, el gerente necesita realizar ciertos cálculos sobre las
edades de estos. En el banco hay 3 tipos de clientes numerados del 1 al 3 según el
tipo de cuenta que poseen. De cada cliente se conoce la siguiente información:
- Nombre del cliente
- Edad (valor entero)
- Tipo_de_cliente (valor entero de 1 a 3)
Para simplificar su trabajo, el gerente te pide que desarrolles una aplicación, que
obtenga los siguientes resultados:
a) La cantidad de clientes por cada tipo de cuenta.
b) La edad del cliente más joven (se supone único).
c) El promedio de las edades, considerando solo a los clientes del tipo 3.
- Se ingresan datos de clientes hasta que el tipo de cuenta sea cero.
  
3. Una cerealera desea clasificar sus clientes de acuerdo con las toneladas que le
compran.
- Cliente que compra menos de 100 toneladas: chico.
- Cliente que compra entre 100 y 300 toneladas: mediano.
- Cliente que compra más de 300 toneladas: grande.
Se desea diseñar un algoritmo que permita el ingreso de las toneladas por cliente y
el tipo de cliente (chico, mediano o grande). Finaliza el ingreso de datos cuando se
ingrese las toneladas igual a 000. Luego muestre la siguiente información por
pantalla:
a) Cantidad de clientes.
b) Calcular el valor total de toneladas vendidas, sabiendo que la tonelada cuesta
250 dólares, y que los clientes grandes tienen un descuento del 5%.
c) Porcentaje de toneladas vendidas por categoría. (cantidad_categoria*100/Total)

4. Un dentista de la zona le solicitó que realice un programa para poder llevar su
agenda de turnos.
En el mismo debe existir un menú para que la secretaria pueda realizar sus tareas
con facilidad, ya que según lo que ella misma informa "la computadora no es su
amiga". En el menú deben visualizarse las siguientes opciones:
- Ingresar turnos
- Ver turnos
- Eliminar turnos cancelados
- Ver estadísticas
- Salir
En cada ítem del menú deberá:
- Ingresar turnos:
El dr. solo atiende 23 pacientes por día, los datos que se registran de cada paciente
son los siguientes:
- Nombre
- Número de socio
- Horario (de 8 a 20hs)
- Tratamiento (Control, arreglo de caries, ortodoncia, extracción)
- Ver turnos: debe mostrar todos los turnos ordenados de menor a mayor
según el horario asignado mostrando todos los datos de cada paciente en
forma prolija y clara.
- Eliminar turnos: si un cliente llama para eliminar el turno, la secretaria le
pedirá su número de socio y eliminará el turno.
- Ver estadísticas:
- Promedio de todos los pacientes que se realizan ortodoncia
- Cantidad de pacientes a atender antes de las 16hs
