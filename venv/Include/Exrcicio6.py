# Melhore o desafio 061, perguntado para o usuário se ele quer mostrar mais alguns termos.O programa qualguer e mostre na tela os n primeiro elemento de uma sequencia de Fibonacci.
# Ex.: 0 > 1 > 2 > 3 > 5 > 8.
    print("---"*30)
    print(" Seguencia de Fibbonaci ")
    print("---"*30)

    n = int(input(" Quantos termos você quer mostrar ? : "))
    t1 = 0
    t2 = 0
    print("~"*30)
    print(f"{t1} -> {t2}",end="")
    cont = 3
    while cont <= n :
        t3 = t1 + t2
        print(f"-> {t3}",end="")
        t1 = t2
        t2 = t3
        cont += 1
    print("-> FIM")
    print("~"*30)