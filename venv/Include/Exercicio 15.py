# 15 - Elaborar um algo para ler o nome e a idade de 2 pessoas e verificar e a masi nova entre as duas pessoas.
nome1 = input(" Entre com o nome : ")
id1 = int(input(" Entre com a idade : "))
nome2 = input(" Entre com segundo nome : ")
id2 = int(input(" Entre com idade : "))
if (id1 > id2) :
    print(" {} com {} é mais velho do que {} com {} anos.".format(nome1,id1,nome2,id2))
elif(id1 < id2) :
    print(" {} com {} é mais novo {} com {}".format(nome1,id1,nome2,id2))
else :
    print(" {} e {} possuem a mesnma idade.".format(nome1,id1,nome2,id2))