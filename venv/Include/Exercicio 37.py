# 37 - Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalos de 1 até 500.
soma, cont = 0,0
for num in range (3,501,3) :
    if (num % 2 == 1) :
        cont += 1
        soma += num
print(f" A soma de todos os {cont} valores é {soma}")