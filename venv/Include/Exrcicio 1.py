# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteaj errada, peça a digidação novamente até ter um valor correto.
sexo = str(input(" Informe seu sexo : [M/F] :")).strip().upper()
while sexo not in " Mm Ff" :
    sexo = str(input(" Dados Inválidos. Por favor, informe seu sexo : ")).strip().upper()[0]
print(f" Sexo {sexo} resgistrado com sucesso. ")
