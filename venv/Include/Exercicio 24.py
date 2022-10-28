# 24 - Crie um programa que leia um número inteiro e mostre na tela se ele é "Par" ou "Impar".
numero = int(input(" Me diga um número qualquer : "))
resultado = numero % 2
if resultado == 0 :
    print(" O núemro {} é par. ".format(numero))
else:
    print(" O número {} é impar.".format(numero))