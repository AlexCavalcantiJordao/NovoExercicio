# 22 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo.
import math
angulo = float(input(" Digite o ângulo que você deseja : "))
tangente = float(input(" Digite a tangente que você deseja : "))
seno = math.sin(math.radians(angulo))
print(" O ângulo de {} tem o seno de {:.2f}.".format(angulo,seno))
tangente = math.tan(math.radians(tangente))
print(" O ângulo de {:.2f} tem a tangente de {:.2f}.".format(tangente,angulo))