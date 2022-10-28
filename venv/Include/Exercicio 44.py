# Faça um programa que leia o peso de cinco pessoas.No final, mostre qual foi o maior e o menor peso lidos.
maior,menor = 0,0
for i in range (1,8,1) :
    peso = float(input(f" Digite o peso da {i}º pessoa :"))
    if (i == 1) :
        maior = peso
        menor = peso
    else:
        if (peso > maior) :
            maior = peso
        if (peso < menor) :
            menor = peso
print(f"\n O maior peso digitado {maior}  ")
print(f"\n O menor peso digitado {menor}  ")