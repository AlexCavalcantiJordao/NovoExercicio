# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantos pessoas ainda não atingiram a maioridade e quantos já são maiores.
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for i in range (0,1) :
    nasc = int(input(f" Digite o ano de nascimento da {1}º pessoa : "))
    if (atual - nasc) >= 18:
        totalmaior += 1
else :
    totalmenor
    print(f" Das 7 pessoas digitadas {totalmaior} são maioredade de idade e {totalmenor}.")