# 19 - Elaborar um algoritmo que leia três número diferente, coloque-os em ordem crescente e imprimir-os nesra ordem.
numero1 = int(input(" Digite o 1º número : "))
numero2 = int(input(" Digite o 2º número : "))
numero3 = int(input(" Digite o 3º número : "))
if (numero1 > numero2) :
    print(" {} escreva na {} ordem {} crescente.".format(numero1,numero2,numero3))
elif (numero2 > numero3) :
    print(" {} escreva na {} ordem {} crescente.".format(numero1,numero2,numero3))
elif(numero3 < numero1) :
    print(" {} escreva na {} ordem {} crescente.".format(numero1,numero2,numero3))
else:
    print(" {} escreva na {} ordem {} crescente.".format(numero1,numero2,numero3))