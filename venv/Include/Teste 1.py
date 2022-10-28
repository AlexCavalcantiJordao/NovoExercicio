teste = list()
teste.append(" Alex ")
teste.append(23)
galera = list()
galera.append(teste[:])
teste[0] = "Pedro"
teste[1] = 22
galera.append(teste[:])
print(galera)