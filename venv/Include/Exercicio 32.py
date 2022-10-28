# 32 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.
# - Se ele ainda vai se alista ao serviço militar.
# - Se é a hora de se alista.
# - Se já passou do tempo do alistamento.
nome = str(input(" Informe o nome : "))
idade = int(input(" Informe a idade : "))
if (idade <= 17) :
    print(" Tem que apresentar no quartel ! ")
elif (idade != 19) :
    print(" Hora de alistar ! ")
elif (idade >= 21) :
    print(" Passou do tempo. Vai pagar a multa ! ")