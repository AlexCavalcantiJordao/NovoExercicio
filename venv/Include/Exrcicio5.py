# Reforça o desafio 051, lendo o 1° termo e a razão de uma P.A, mostrado os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input(" 1° termo : "))
razão = int(input(" Razão : "))
decimo = primeiro +(10 - 1)* razão
for c in range(primeiro,decimo + razão, razão) :
    print(f"{c}",end=" ---> ")
print(" Acabou ! ")