# 30 - Escreva um prograama que leia um número inteiro qualquer e peça para o usuário escolhar qual será a base de conversão.
# 1 para binario, 2 para octal, 3 para hexadecimal

num = int(input(" Digite um número inteiro : "))
print(" Escolha uma das bases para conversão : [1] coverter para binário, [2] Coverter para octal, [3] coverter para hexadecimal. ")
opção = int(input(" Sua opção : "))
if opção == 1 :
    print(" {} covertido para binário é igual a {}.".format(num,bin(num)[2:]))
if opção == 2 :
    print(" {} covertido para octal é igual a {}.".format(num,oct(num)[2:]))
if opção == 3 :
    print(" {} convertido para hexadecimal é igual a {}.".format(num,hex(num)[2:]))
else :
    print(" Opção inválido.Tente novamente. ")