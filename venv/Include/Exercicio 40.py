# Desenvolvar um programa que leia o primeiro termo e a razão de um P.A.No final,mostre os 10 primeiro termo dessa progressão.
primeiro = int(input(" 1º termo : "))
razao = int(input(" Razão : "))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro,decimo + razao,razao) :
    print(f"{c}", end= " -> ")
    print(" Acabou ")