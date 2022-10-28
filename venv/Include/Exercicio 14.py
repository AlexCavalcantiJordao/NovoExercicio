# 14 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e toda as informação possiveis sobre ele.
algo = input(" Digite algo : ")
print(" O tipo primitivo desse valor {} é : {} \n".isspace())
print(" {} È um número ? {}".format(algo,algo.isnumeric()))
print(" {} È alfabético ? ".format(algo,algo.isalpha()))
print(" {} È alfanumerico ? ".format(algo,algo.isalnum()))
print(" {} Está em maiúsculo ? ".format(algo,algo.isupper()))
print(" {} Está em minusculo ? ".format(algo,algo.islower()))
print(" {} Está capitalizado ? ".format(algo,algo.istitle()))