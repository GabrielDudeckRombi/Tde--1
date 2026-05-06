import numpy as np

# 1. Soma Total: Crie uma matriz 3 x 3 de números inteiros e exiba a soma de
# todos os elementos.

# matriz = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8 ,9]])

# print(matriz)

# 2. Identidade: Peça ao usuário um valor n e gere uma Matriz Identidade de
# ordem n.

# n = int(input("Informe o valor de n para gerar a matriz: "))

# matriz = []

# for i in range(n):
#     linha = []
#     for j in range(n):
#         if i == j:
#             linha.append(1)
#         else:
#             linha.append(0)
#     matriz.append(linha)

# for linha in matriz:
#     print(linha)

# 3. Busca Simples: Dada uma matriz 4 x 4, peça um número ao usuário e diga
# se esse número está ou não na matriz.

# matriz = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10 ,11, 12],
#                 [12, 13, 14, 15]])

# n = int(input("Informe um numero para ver se ele esta na matriz: "))

# if n in matriz:
#     print(f"O numero {n} esta na matriz")

# else:
#     print(f"Esse numero {n} nao esta na matriz")

# 4. Troca de Valores: Crie uma matriz 2 x 2 e troque os valores da primeira linha
# com os da segunda linha.

# matriz = np.array([[1, 2],
#                 [3, 4]])

# matriz[[0, 1]] = matriz[[1, 0]]

# print(matriz)

# 5. Multiplicação por Escalar: Leia uma matriz 3 x 3 e um número real. Exiba a
# matriz resultante da multiplicação de cada elemento por esse número.

# matriz = np.array([[0, 1, 2],
#                 [4, 5 ,6],
#                 [7, 8 ,9]])

# escalar = float(input("Digite o numero que ira multiplicar os numeros da matriz: "))

# resultado = matriz * escalar

# print(resultado)

# 6. Contagem de Pares: Dada uma matriz 3 x 4, conte quantos números pares
# ela possui.

# matriz = ([[0, 1, 2, ],
#         [3, 4, 5],
#         [6, 7, 8],
#         [9, 10 , 11]])

# contador = 0

# for linha in matriz:
#     for elemento in linha:
#         if elemento % 2 == 0:
#             contador += 1

# print(f"A quantidade de pares e: {contador}")

# 7. Maior Elemento: Crie uma matriz preenchida com números aleatórios e
# encontre qual é o maior valor presente nela.

# matriz = np.array([[10, 20 ,30],
#                 [40, 70, 100],
#                 [40, 50, 90]])

# maior = matriz[0][0]

# for linha in matriz:
#     for elemento in linha:
#         if elemento > maior:
#             maior = elemento

# print(f"O maior elemento: {maior}")

# 8. Média por Linha: Crie uma matriz 3 x 3 e exiba a média aritmética dos
# valores de cada linha separadamente.

# matriz = np.array([[1, 2, 3,],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# medias = matriz.mean(axis=1)

# print(medias)

# 9. Soma da Diagonal Principal: Calcule a soma de todos os elementos que
# compõem a diagonal principal de uma matriz 4 x 4.

# matriz = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10 , 11 ,12],
#                 [13, 14, 15, 16]])

# soma = matriz.diagonal().sum()

# print(soma)

# 10. Matriz Transposta: Escreva um programa que receba uma matriz M x N e
# gere a sua transposta (N x M).

# matriz = np.array([[1, 2 , 3],
#                 [4, 5, 6]])

# tranposta = matriz.T

# print(tranposta)

# 11. Soma de Colunas: Crie uma matriz 3 x 3 e gere uma lista (array) de 3
# elementos onde cada elemento é a soma de uma coluna da matriz.

# matriz = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# soma_colunas = matriz.sum(axis=0)

# lista = []

# lista.append(soma_colunas)

# print(lista)

# 12. Verificação de Simetria: Verifique se uma matriz quadrada é simétrica (onde
# a matriz é igual à sua transposta).

# matriz = np.array([[1, 2, 3],
#                 [2, 5, 6],
#                 [3, 6, 9]])

# if np.array_equal(matriz, matriz.T):
#     print("A matriz e simetrica")

# else:
#     print("A matriz nao e simetrica")

# 13. Diagonal Secundária: Exiba apenas os elementos da diagonal secundária
# de uma matriz 5 x 5.

# matriz = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15],
#                 [16, 17, 18, 19, 20],
#                 [21, 22, 23, 24, 25]])

# diagonal_secundaria = np.fliplr(matriz).diagonal()

# print(diagonal_secundaria)

# 14. Multiplicação de Matrizes: Implemente a multiplicação de duas matrizes.
# Lembre-se: para multiplicar A por B, o número de colunas de A deve ser igual
# ao número de linhas de B.

# matriz1 = np.array([[1, 2, 3],
#                     [4, 5, 6]])

# matriz2 = np.array([[7, 8, ],
#                     [9, 10 ],
#                     [11, 12]])

# resultado = np.dot(matriz1, matriz2)

# print(resultado)


# 15. Rotação 90°: Crie um algoritmo que rotaciona uma matriz quadrada n x n em
# 90 graus no sentido horário (sem usar bibliotecas prontas como NumPy)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matriz)
rotacionada = []

for j in range(n):
    nova_linha = []
    for i in range(n - 1, -1, -1):
        nova_linha.append(matriz[i][j])
    rotacionada.append(nova_linha)

for linha in rotacionada:
    print(linha)

    #ex_matriz