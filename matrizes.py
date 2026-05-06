import numpy as np

# x = np.zeros((2, 3))
# print(x)

# y = np.ones((3, 2))
# print(y)

# z = np.eye(3)
# print(z)

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# elemento = matriz[1][2]
# print("Elemento:", elemento)

# matriz[0][1] = 9
# print("Matriz modificada: ", matriz)

# a = np.array([1, 2, 3],
#             [4, 5, 6])

# b = np.array([7, 8, 9],
#             [10, 11 ,12])

# print(f"Soma das marizes: {}")


# Aula 6

# Matrizes - Exercícios de fixação
# Obs.: use import numpy as np no início de cada script/algoritmo

# 1. Você faz parte de uma equipe que monitora a quantidade de chuva
# em uma cidade ao longo de alguns dias. Para isso, os dados são
# organizados em matrizes, onde:
# • Cada linha representa um dia.
# • Cada coluna representa uma região da cidade.
# Você recebeu duas matrizes:
# • A primeira representa a quantidade de chuva (em mm) registrada na
# parte da manhã.
# • A segunda representa a quantidade de chuva registrada na parte da
# tarde.

# Crie um algoritmo em Python utilizando NumPy que:
# • Cria duas matrizes 3x3:
# • manha,
# • tarde.
# • Some as duas matrizes para obter a matriz total, que representa a
# quantidade total de chuva por dia e por região.
# Exiba:
# • A matriz da manhã.
# • A matriz da tarde.
# • A matriz total (resultado da soma).

# manha = np.array([[20 , 30 , 25],
#                 [30, 45, 20],
#                 [20, 30 ,40]])

# tarde = np.array([[30, 40, 24],
#                 [30, 22, 80],
#                 [20, 70, 20]])

# soma_matriz = manha + tarde

# print(f"A matriz da {manha}")
# print()
# print(f"A matriz da {tarde}")
# print()
# print(f"A soma das duas matrizes de manha e tarde e: {soma_matriz}")

# 2. Você trabalha no controle de estoque de uma loja:
# • Uma matriz representa a quantidade de produtos antes das vendas.
# • Outra matriz representa a quantidade de produtos vendidos.
# Crie um algoritmo em Python com NumPy que:
# • Crie duas matrizes 3x3:
# • estoque_inicial.
# • vendidos.

# Calcule a matriz estoque_final, subtraindo:
# estoque_final = estoque_inicial - vendidos.
# Exiba:
# • Todas as matrizes.

# estoque_inical = np.array([[20, 30 , 40],
#                         [40, 20, 30],
#                         [30, 40, 20]])

# vendidos = np.array([[10, 15, 20],
#                     [20, 7, 9],
#                     [10, 7, 10]])

# estoque_final = estoque_inical - vendidos

# print("Estoque inicial")
# print(estoque_inical)

# print()

# print("Vedidos")
# print(vendidos)

# print()

# print("Estoque final")
# print(estoque_final)

# 3. Você está ajudando a montar um sistema de uma lanchonete:
# • Uma matriz representa quantidade de ingredientes por lanche.
# • Outra matriz representa quantidade de lanches pedidos.
# Crie:
# • Uma matriz ingredientes (ex.: 2x3).
# • Uma matriz pedidos (ex.: 3x2).
# Realize a multiplicação das matrizes e exiba o resultado

# ingredientes = np.array([[10, 20],
#                         [20, 10],
#                         [12, 18]])

# pedidos = np.array([[7, 10, 16],
#                     [10, 8, 9]])

# resultado = np.dot(ingredientes, pedidos)

# print("Ingredientes")
# print(ingredientes)

# print("\nPedidos")
# print(pedidos)

# print("\nResultado")
# print(resultado)

# 4. Você trabalha no RH de uma empresa. A matriz representa os
# salários de funcionários em diferentes setores. A empresa decidiu
# aplicar um aumento de 10% para todos.
# Crie:
# • Uma matriz 3x3 chamada salarios.
# • Multiplique toda a matriz por 1.10.
# # • Exiba a matriz original e a matriz reajustada

# salarios = np.array([[1620, 3000, 100000],
#                     [9000, 8000, 5000],
#                     [4000, 15000, 50000]])

# salarios_reajustados = salarios * 1.10

# print("Salarios Originais")
# print(salarios)

# print("\n Salarios depois de reajuste de 10%")
# print(salarios_reajustados)


# 5. Você está reiniciando um sistema que armazena dados temporários.
# Para limpar tudo, precisa zerar a matriz.
# Crie:
# • Uma matriz 3x3 com valores quaisquer.
# • Transforme todos os valores da matriz em 0.
# • Exiba a matriz final.

# dados = np.array([[10, 20, 30],
#                 [30, 50, 60],
#                 [70, 80, 90]])

# clear = dados * 0

# print(dados)

# print()

# print(clear)

# 6. Um sistema foi iniciado e todos os sensores precisam começar
# ativos. Na matriz, 1 significa ativo.
# Crie:
# • Uma matriz 4x4 com valores quaisquer.
# • Altere todos os valores da matriz para 1.
# • Exiba a matriz final.

# sistema = np.array([[10, 20, 0, 11],
#                     [10, 15 , 77, 33],
#                     [50, 90, 22, 11]])

# print(sistema)

# sistema[:] = 1

# print()

# print(sistema)

# 7. Você encontrou um erro em um sistema: um valor específico da
# matriz está incorreto.
# Crie:
# • Uma matriz 5x5 com valores inteiros.
# • Substitua o valor das posições:
# • Linha 1, coluna 2.
# • Linha 3, coluna 5.
# • Defina novos valores para essas posições.
# • Exiba a matriz antes e depois da alteração.

dados = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]])

print("Matriz antes errada")
print(dados)

dados[0][1] = 99
dados[2][3] = 77

print("\n Matriz apos correcao dos erros:")
print(dados)

#
#new commit