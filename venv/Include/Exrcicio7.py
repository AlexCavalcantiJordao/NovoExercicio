# Melhore o desafio 061, perguntado para o usuário se ele quer mostrar mais aluns termos.O programa encerra quando ele disse que quer mostrar 0 termo.
num = cont = soma = 0
num = int(input("Digite um número [999 Para parar] : "))
while num != 999 :
    soma + num
    cont += 1
    num = int(input("Digite um número [999 Para parar] : "))
print(f"\n Você digitou {cont} número e a soma entre eles foi {soma}. ")
