# 11 - Elaborarum algoritmo que leia número inteiro maiores ou iguais a 0 e menores e igual ou igual a 10.
contador = 0
referencia = int(input(" Entre com o número de referencia : "))
produto = 1
for i in range (10) :
    num = int(input(" Entre com um número : "))
    if num > referencia :
        if (num % 5 == 0) and (num % 2 == 0) :
            produto *= num
print("\n Produto : ", produto)