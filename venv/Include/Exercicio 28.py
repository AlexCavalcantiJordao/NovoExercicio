# 28 - Faça um programa que leia três número e mostre qual é o maior e qual é o menor.
a = int(input(" Primeiro valor : "))
b = int(input(" Segundo valor : "))
c = int(input(" Terceiro valor : "))
menor = a
if b < a and b < c :
    menor = b
elif c < a and c < b :
    menor = c
    # verificar quem é maior
maior = a
if b > a and b > c :
    maior = b
elif c > a and c > b :
    maior = c
print(" O menor valor digitado foi {} e maior valor digitado {}. ".format(menor,maior))