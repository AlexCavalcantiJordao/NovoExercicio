# 21 - Faça um programa que leia o comprimento de cateto oposto e do cateto adjcente de um triângulo retângulo, calcule e mostre o comprimento da hiotenusa.
co = float(input(" Comprimento do cateto oposto : "))
ca = float(input(" Comprimento do cateto adjacente : "))
h1 = (co**2 + ca**2)**(1/2)
print(" A hipotenusa vai medir {:.2f}.".format((h1)))