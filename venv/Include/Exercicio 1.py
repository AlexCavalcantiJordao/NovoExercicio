# 1 - Elabora um algoritmo para ler cinco valores reais, calcular e imprimir os número lidos os números e a media desses valores.

nota1 = float(input(" Nota 1 : "))
nota2 = float(input(" Nota 2 : "))
simulado = float(input(" Nota simulado "))
ac1 = float(input(" Nota ac1 : "))
ac2 = float(input(" Nota ac2 : "))
media1 = (nota1 + nota2)/2
mediaac = (ac1 + ac2)/2
mediaf = (media1 + simulado + mediaac)/3
print(mediaf)
if mediaf == 6 :
    print(" Na media ")
if mediaf < 6 :
    print(" Abaixo da media")