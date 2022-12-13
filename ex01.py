#
# autor: michel

# data: 13/12/2022

# matriz de ordem = 3
m1 = [[1,2,3],[4,5,6],[7,8,9]]

                  # ij ij ij
                #1  00 01 02
                #2  10 11 12
                #3  20 21 22
                # abaixo DP (i > j)
                # DS (i+j) == (ordem - 1)
                # Acima DS (i + j) <= (ordem - 2)
                # abaixo DS (i + j) >= (ordem)
m2 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

ordem = 3

# a) calcular a soma dos elementos da matriz
somaTotal = 0
for i in range(ordem):
  for j in range(ordem):
    somaTotal += m1[i][j]

print(f'soma Total = {somaTotal}')

# b) calcular a soma da linha 1 da matriz
somaLinha1 = 0
for i in range(ordem):
  for j in range(ordem):
    if i == 0:
      somaLinha1 += m1[i][j]

print(f'soma linha 1 = {somaLinha1}')

# c) calcular a soma da coluna 2 da matriz
somaColuna2 = 0
for i in range(ordem):
  for j in range(ordem):
    if j == 1:
      somaColuna2 += m1[i][j]

print(f'soma coluna 1 = {somaColuna2}')

# d) calcular a soma dos elementos acima da DP da matriz
somaAcimaDP = 0
for i in range(ordem):
  for j in range(ordem):
    if i < j:
      somaAcimaDP += m1[i][j]

print(f'soma Acima DP = {somaAcimaDP}')

# e) calcular a soma dos elementos acima da DS da matriz
somaAcimaDS = 0
for i in range(ordem):
  for j in range(ordem):
    if (i + j) <= (ordem - 2):
      somaAcimaDS += m1[i][j]

print(f'soma Acima DS = {somaAcimaDS}')

# f) calcular o quadrado dos elementos acima da DS da matriz,
# adicionando em uma nova lista (apenas esses elementos).
novaLista = []
for i in range(ordem):
  for j in range(ordem):
    if (i + j) <= (ordem - 2):
      novaLista.append(m1[i][j]**2)

print(f'nova lista = {novaLista}')