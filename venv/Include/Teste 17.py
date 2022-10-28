# Aprimore o Desafio 093 para que ele funciona com vários jogador, incluido um sistema de visualização de detalhe do aproveitamento de cada jogador.
time = list()
jogador = dict()
partida = list()

while True :
    jogador.clear()
    jogador['nome'] = str(input(" Nome do jogador : "))
    tot = int(input(f" Quantas partidas {jogador['nome']} jogou ? : "))
    partida.clear()
    for c in range(0,tot) :
        partida.append(int(input(f"   Quantos gols na partida {c+1} ? : ")))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True :
        resp = str(input(" Quer continuar ? [S/N] : ")).upper()[0]
        if resp in "SN" :
            break
        print(" ERRO ! Responda apenas S ou N. ")
    if resp == "N" :
        break
print("=<=>="*25)
print(" cod ",end="")
for i in jogador.keys() :
    print(f"{i:<15}",end=" ")
print()
print("=<=>="*25)
while True :
    busca = int(input(" Mostrar dados de qual jogador ? ( 999 para parar ) :  "))
    if busca >= len(time) :
        print(f" ERRO ! Não existe jogador com código {busca} ! ")
    else:
        print(f"--- LEVANTAMENTO DO JOGADOR {time[busca]['nome']} : ")
        for i, g in enumerate(time[busca]['gols']) :
            print(f"  No jogo {i+1} fez {g} gols. ")
    print("=<=>="*25)
print(" <<< VOLTE SEMPRE >>>")
