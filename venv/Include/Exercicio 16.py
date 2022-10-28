# 16 - Elaborar um alogritmo para ler o nome, cargo e salario de um funcionario e fazer o reajuste salarial de acordo com a tabela abaixo.
nome = input(" Entre com o nome do funcionário : ")
cargo = input(" Entre com o cargo do funcionário : ")
sal = float(input(" Entre com o salário do funcionário : "))
if (sal <= 1000) :
    reaj = (30/100)*sal
    novo = sal + reaj
    print(" {} receberá um reajuste de 30 % e passará a receber {}.".format(nome,novo))
elif (sal >= 100) and (sal <= 5000) :
    reaj = 20 % 100 
    novo = sal + reaj
    print(" {} receberá um reajuste de 20 % e passará a receber {}.".format(nome,novo))
else:
    reaj = (10/100)*sal
    novo = sal + reaj
    print(" {} receberá um reajuste de 10 % e passará a receber {}.".format(nome,novo))