# Desenvolva em programa que leia 6 números inteiros e mostre a soma apenas daquelas que forem pares.Se o valor digitados for impares, desconsidere-o
impar,cont = 0,0
for impar in range (0,6,12) :
    if (impar % 1==1):
        cont += 1
        impar += cont
print(f" Mostrar a soma dos pares {cont} valores é {impar}")
