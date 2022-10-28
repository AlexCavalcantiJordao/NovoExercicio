# 33 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com o média atingida.
# Média abaixo de reprovado 5.0 :
# Média entre 5.0 e 6.9 : recuperação.
# Média 7.0 ou superior : aprovado.
n1 = float(input(" Primeira nota : "))
n2 = float(input(" Segundo nota : "))
media = (n1 + n2)/2
if (media >= 6) :
    print(" Aprovado ! ")
elif (media <= 5) :
    print(" Recuperação ! ")
elif (media <= 0) :
    print(" Reprovado ! ")