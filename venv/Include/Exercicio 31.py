# 31 - Escreva um programa que leia dois número inteiro e compare-os, mostrando na tela uma mensagem :
# - O primeiro valor é maior. - Segundo vakor é maior. - Não existe valor maior, os dois são iguais.
n1 = int(input(" Primeiro número : "))
n2 = int(input(" Segundo número : "))
if (n1 > n2) :
    print(f" O primeiro é maior {n1} do que {n2} segundo.")
else :
    print(f" {n1} e {n2} são iguais.")