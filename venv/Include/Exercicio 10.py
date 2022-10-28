# 10 - Crie um programa que leia um número e mostre o seu dobro.Triplo e raiz quadrada
import math
num = float(input(" Entre com um número : "))
dobro = 2*num
triplo = 3*num
raiz = math.sqrt(num)
print(" O dobro de {} é {}.".format(num,dobro))
print(" O triplo de {} é {}.".format(num,triplo))
print(" A raiz quadrada de {} é {:.3}.".format(num,raiz))