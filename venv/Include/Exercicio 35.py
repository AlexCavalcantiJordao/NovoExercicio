# 35 - Fça em programa que mostre na tela uma contagem regressiva para a estouro de fogos de artificios, indo de 10 até 0. com uma pausa de 1 segundo entre eles.
from time import sleep
print(" Contagem Regressiva : ")
for i in range (10,1,-2) :
    print(i)
    sleep(i)
print(" Execelente ! ")