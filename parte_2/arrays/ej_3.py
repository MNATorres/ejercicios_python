# 3) Dados dos arreglo s A y B de N<15 elementos cada uno, calcular un arreglo C tal que C 
# = A + B.


A = []
B = []

for i in range(0, 14):
    A.append(i + 1)
    B.append(i + 1)
    
C = A + B

print(f"Este es A {A}")
print(f"Este es B {B}")
print(f"Este es C {C}")