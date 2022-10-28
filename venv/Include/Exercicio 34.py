# 34 - A confederação nacional de natação precisa de um programa que leia o um atleta e mostre sua categoria, de acordo com a idade.
# Até 9 anos : mirim.
# Até 14 anos : infantil.
# Até 19 anos : junior.
# Acima : master
from datetime import date
atual = date.today().year
nascimento = int(input(" Ano de nascimento : "))
idade = atual - nascimento
print(f" O atleta tem {idade} anos.")
if idade <= 9 :
    print(" Classificação : Mirim ! ")
elif idade <= 14 :
    print(" Classificação : Infantil ! ")
elif idade <= 19 :
    print(" Classificação : sênior ! ")
else:
    print(" Classificação : Master ! ")