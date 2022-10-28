# Escreva um programa que leia vários números inteiros pelo teclados. O programa vai parar quando o usuário digitar o valor 999, que é a condição de parada.
soma = cont = 0
while True :
    num = int(input(" Digite um valor [999 Para parar] : "))
    if num == 999 :
        break
    cont += 1
    soma += num
print(f"\n A soma dos números {cont} valores foi {soma} ! ")