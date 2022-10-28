# Crie um programa que leia nome, sexo e idade de vários pessoas, quadrado os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.No final,mostre:
# a) Quantos pessoas foram cadastrados.
# b) A média de idade do grupo.
# c) Uma lista com todas as pessoas as pessoas com idade acima da média.
# d) Uma lista com todas as pessoas com idade acima da média
pessoa = dict()
galera = list()
while True :
    pessoa.clear()
    pessoa['nome'] = str(input(" Nome : "))
    while True :
        pessoa['sexo'] = str(input(" Sexo : [M/F] : ")).upper()[0]
        if pessoa['sexo'] in 'MF' :
            break
        print(" ERRO ! Por Favor, Digite apenas M ou F. ")
    pessoa['idade'] = int(input(" Idade :"))
    galera.append(pessoa.copy())
    while True :
        resp = str(input(" Quer continuar ? [S/N] : ")).upper()[0]
        if resp in "SN" :
            break
        print(" ERRO ! Responda apenas S ou N. ")
    if resp == "N" :
        break
print("-="*30)
print(f" A) Ao todo temos {len(galera)} pessoa cadastrados. ")
média = soma / len(galera)
print(f" B) A média de idade é de {média:5.2f} anos. ")
print(" c) As mulheres cadastrados foram ",end=" ")
for p in galera :
    if p['sexo'] in "Ff" :
        print(f" {p['nome']}",end=" ")
print()
print(" D) Lista das pessoas que estão acima da média : ")
for p in galera :
    if p['galera'] >= média :
        print("   ")
        for k, v in p.items() :
            print(f"{k} = {v}",end=" ")
    print()
print("<<< ENCERRADO >>>")