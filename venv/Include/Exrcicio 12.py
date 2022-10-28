    # Elaborar um algoritmo que recebar a idade e o estado civil (c-casado, s-solteiro, v- viuvo(a) e d-desquitado), lidos nessa ordem.
casados,casados_30,solteiro,solteiro_22,viuvos,soma_viuvos,desquitados = 0,0,0,0,0,0,0
while True :
        idade = int(input(" Entre com a idade : "))
        if idade == 0 :
            break
        elif idade < 0 :
            print(" Idade inválida, tente novamente. ")
        continue
    while True :
        estado_civil
        input(" Entre com estado civil (C,S,V,D) : ").upper()

        if estado_civil == "c" :
            casados += 1

        elif estado_civil == "s" :
            solteiro +=1

        if  idade > 22 :
            solteiro_22 += 1

        elif estado_civil == "v" :
            viuvos += 1

            soma_viuvos += idade

        elif estado_civil == "d" :
            desquitados += 1

        else :
            continue
        break

        total = casados + solteiros + viuvos + desiquitados

    print()
print(casados_30," pessoas são casados e tem 30 ou menos anos.")
print(solteiro_22," pessoas são solteirose tem 22 ou mais anos.")
if viuvos > 0 :
        print(f" Os viuvos tem um média {soma_viuvos/viuvos:.1f} anos.")
    else :
        print(" Nenhum viúvos foi digitados. ")
        print(f" {desquitados/total*100:.1f} % pessoas são desquitados. ")