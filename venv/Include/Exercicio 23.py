# 23 - Um professor quer sortear um dos seus quatros o aluno apagar o quadro. Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = str(input(" 1º Aluno : "))
n2 = str(input(" 2º Aluno : "))
n3 = str(input(" 3º Aluno : "))
n4 = str(input(" 4º Aluno : "))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(" A ordem de apresentação.")
print(lista)