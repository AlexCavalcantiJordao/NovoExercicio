# 9 - Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e antecessor.
num = int(input(" Entre com um número : "))
ant = num - 1
suc = ant + 1
print(" O antecessor do número {} è {} : ".format(num,ant))
print(" O sucessor do número {} é {} : ".format(num,suc))