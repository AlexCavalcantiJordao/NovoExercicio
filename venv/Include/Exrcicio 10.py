# 10 - Crie um prograama que leia varios números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual o maior e o menor valores lidos.
maior,menor = 0,0
num = int(input(" Entre com um número : "))
while (True) :
    op = input(" Deseja continuar ? ")
    if (op == "n") :
        break

    if (num > maior) :
        maior = num

    if (num < menor) :
        menor = num

    num = int(input(" Entre com um número : "))