# 18 - Elaborar um algoritmo para imprimir o maior valor entre três valores lidos, sem levar em consideração a leitura de valores iguais.
n1 = int(input(" Entre com um número : "))
n2 = int(input(" Entre com 2º número : "))
n3 = int(input(" Entre com 3º número : "))
if (n1 > n2) :
    print(" O primeiro é maior {} do que segundo {} do que terceiro {} ".format(n1,n2,n3))
elif(n3 > n2) :
    print(" Terceiro {} é menor do que {} segundo.".format(n3,n2))
else :
    print(" {}, {} e {} são iguais.".format(n1,n2,n3))