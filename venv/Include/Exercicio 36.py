# Crie um programa que mostre na tela todos os números pares que estão no intervelos entre 1 e 50.
soma = 0
for num in range (0,6,1) :
    num = int(input(" Digite um número : "))
    if num % 2 == 0 :
        soma = num + soma
        print(f" Soma dos pares {soma}")
