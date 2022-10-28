# Faça um programa que leia um número inteiro e doga se ele é ou não um primo.
primeiro = int(input(" Primeiro termo : "))
cont = 0
for i in range (1,cont+ 1,1) :
    if (cont % i == 0) :
        cont += 1
    if (cont == 2) :
        print(f" Número é primo {cont}")
else :
    print(f" Não é primo {cont}")