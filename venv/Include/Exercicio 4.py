# 4 - Elaborar um algoritmo para ler o saldo de um aplicação e imprimir o saldo, valor do reajuste e o novo saldo. Considerando que o valor doi de 5%.
x = int(input(" Digite o reajuste : "))
y = int(input(" Digite o novo reajuste : "))
reajuste = (x+y)/5
print(" Reajuste é : {}.".format(reajuste))