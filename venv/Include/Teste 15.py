# Crie um progrma que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantos partidas e ele jogou. Depois vai ler a quantidades gols feitos em cada partidas.Nos final, tudo isso será quantidades em um dicionario, incluido o total de gols feitos durante o campeonato.
jogador = dict()
partida = list()
jogador['nome'] = str(input(" Nome do jogador : "))
tot = int(input(f" Quantas partidas {jogador['nome']} jogou ? : "))
for c in range(0, tot) :
    partida.append(int(input(f"    Quantos gols na partida {c} ? : ")))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print("=-="*30)
print(jogador)
print("=-="*30)
print(f" O jogador {jogador['nome']} jogou {len('gols')} partidas.")
for i, v in enumerate(jogador['gols']) :
    print(f"    => Na partida {i},fez {v} gols.")
print(f" Foi um total de {jogador['total']} gols.")