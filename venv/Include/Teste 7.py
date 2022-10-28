# crie um programa onde o usuario possa digitar sete valores numerico e cadastre-os em uma lista unica que mantenha separado os valores pares e impares. No final, mostre os valores pares e impares em ordem
num = [[], []]
valores = 0
for c in range (1,8) :
    valor = int(input(f" Digite o {c}°. valor : "))
    if valor % 2 == 0 :
        num[0].append(valor)
    else :
        num[1].append(valor)
print("-="*30)
print(f" Os valores pares digitados foram : {num[0]}")
print(f" Os valores impares digitados foram : {num[1]}")