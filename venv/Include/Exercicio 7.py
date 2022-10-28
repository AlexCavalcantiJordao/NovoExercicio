# 7 - Elaborar um algoritmo para ler um numero inteiro de 3 casas decimais e imprimir dos algoritmo casas dezenas e das unidades.
num = float(input(" Entre com o numero com 3 casas decimais : "))
cent = num // 100
resto = num % 100
dez = resto // 10
uni = resto % 10
soma = dez + uni
print(" Centenas : {}, dezenas : {}, unidade {}: ".format(cent, dez, uni))
print(" Soma dos algoritmo : {}.".format(soma))