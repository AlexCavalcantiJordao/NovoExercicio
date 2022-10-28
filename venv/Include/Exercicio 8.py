# 8 - Elaborar um algoritmo para calcular e imprimir x = (A+B) / (A-B), sabendo-se que A e B são numeros nunmeros reais lidos do teclado.
A = int(input(" Digite o valor A : "))
B = int(input(" Digite o valor B : "))
print(" Valores originais A : {} e B {}.".format(A,B))
aux = A
A = B
B = aux
print(" Valores trocados - A : {} e B {}.".format(A,B))