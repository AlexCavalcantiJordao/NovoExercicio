# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se for o acaso á CTPS for diferente de 0, o dicionario receberá também o nao de contratação eo salário.
from datetime import datetime
dados = dict()
dados['nome'] = str(input(" Nome : "))
nasc = int(input(" Ano de nascimento : "))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input(" Carteira de Trabalho ( 0 não têm ) : "))
if dados['CTPS'] != 0 :
    dados['contratação'] = int(input(" Ano de Contratação : "))
    dados['salário'] = float(input(" Salário : R$ "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print("-="*30)
for k, v in dados.items() :
    print(f" - {k} tem o valor {v}")