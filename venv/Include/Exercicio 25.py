# 25 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custa R$ 7,00 pro cada km acima do limite.
velocidade = float(input(" Qual é a velocidade atual do carro ? : "))
if velocidade > 80 :
    print(" Multado ! Você excedeu o limite permitido que é de 80 KM/H.")
multa = (velocidade - 80)*7
print(" Você deve pagar uma multa de R$ {:.2f} !".format(multa))
print(" Tenha um bom Dia ! Dirija com segurança ! ")