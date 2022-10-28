# 26 - Desenvolva um programa que pergunta a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagem de até 200 KM e R$ 0,45 para viagem mais longas.
distancias = float(input(" Qual é a distâncias da sua viagem : "))
print(f" Você está prestes a começar uma viagem de {distancias} KM.")
if distancias <= 200 :
    preco = distancias *0.50
else:
    print(" É o preço da sua passagem será de R$ {:.2f}.".format(distancias))