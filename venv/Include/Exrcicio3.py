# Crie um programa que leia 2 valores e mostre um menu na tela.
# [1] Somar, [2] Multiplicar, [3] Maior, [4] Novo Número, [5] Sair do programas
from time import sleep
n1 = int(input(" 1° número : "))
n2 = int(input(" 2º número : "))
opção = 0
while opção != 5 :
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos Números")
    print("[5] Sair do programa")

opção = int(input(" Qual é a sua opção ? : "))
if opção == 1 :
    soma = n1 + n2
    print(f" A soma entre {n1} + {n2} = {soma}.")
elif opção == 2 :
    produto  = n1 * n2
    print(f" O resultado de {n1} * {n2} = {produto}.")
elif opção == 3 :
    if n1 > n2 :
        maior = n1
    else :
        maior = n2
        print(f" Entre {n1} e {n2} o maior valor é {maior}")
elif opção == 4 :
    print(" Informe os número novamente : ")
    n1 = int(input(" 1° valor : "))
    n2 = int(input(" 2º valor : "))
elif opção == 5 :
    print(" Finalizando...")
else:
    print(" Opção inválida.Tente novamente ")
    print(" Fim do programa ! Volte Sempre")
