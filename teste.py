# lista = [5, 10]
# lista.append(15)
# print(len(lista))

# #O resultado sera 3 

# lista = [1, 2, 3]
# lista.insert(1, 10)
# print(lista)

# #O resultado ser [1, 10, 2, 3] O Insert o primeiro valor e a pocisao e o do lado e o que vai ser inserido

# lista = [2, 4, 6]
# print(lista[1] * 2)

# # 8


# dados = {'x': 1, 'y': 2}
# print(dados['x'] + dados['y'] )
# 3

# dados = {'a': 10}
# print(dados.get('b', 5))
# Ira retornar 5

# nums = [1, 2, 3]
# total = 0
# for n in nums:
#     total += n
# print(total)
# Ira retornar 6 porque 0 += 0, 0 += 1, 1+= 2, 3+= 3 = 6

# nums = [1, 2, 3, 4]
# soma = 0
# for i in range(len(nums)):
#     soma += nums[i] #Esse [i] pega o valor do numero na lista
#     print(soma)
    # A soma ficaria 0 + 1 = 1
    # 1 + 2 = 3
    # 3 + 3 = 6
    # 6 + 4 = 10

# lista = [10, 20, 30]
# lista.pop(0)
# print(lista)
# o .pop(indice) vai ficar [20, 30]


# lista = [1, 2, 3]
# lista2 = lista # Esse = aponta a msm memoria para as 2 listas lista2= lista.copy() ou lista2 = lista[:]
# lista2.append(4)
# print(lista)
# [1, 2, 3, 4]

# dados = {"nome": "Joao"}
# dados['idade']= 25 # Adiciona a idade do joao no dicionario
# print(dados)
# O print sera ['nome': 'Joao', 'idade': 25]

# import numpy as np
# m = np.array([[1, 2], 
#             [3, 4]])
# print(m[0, 1]) # o print vai ser 2 [linha, coluna]


# import numpy as np

# m = np.array([[1, 2, 3],
#             [4, 5, 6]])

# print(m[1])#Vai printar o indice da coluna variavel m[pocisao]

# dados = {'a': 1}
# dados['a'] = dados['a'] + 5 # Faz a soma da variavel 'a' do dicionario
# print(dados['a']) # vai printar 6

# lista = [2, 4, 6, 8]
# print(lista[-1]) # vai printar 8 pq o negativo seria rodar o indice para tras do 0

# lista = [1, 2, 3]
# del lista[1] 
# print(lista) # vai printar so [1, 3] porque o del delta o valor do indice selecionado

# nums = [1, 3, 5]
# for n in nums:
#     print(n * 2)
#     # 2
#     # 6
#     # 10

# dados = {'x', 10}
# print('x' in dados)
# Vai retornar um bool de acordo com o resultado se tiverr o parametro 'x' no dicionario vai retornar TRUE caso n esteja vai retornar False

# dados = {'a': 1, 'b': 2}
# print(len(dados))
# vai printar 2 

# lista = [10, 20, 30]
# print(lista[1:]) # lista[indice 1  : e ate chegar ao final da lista]

# import numpy as np

# m = np.array([[1, 2],
#             [3, 4]])
# print(m[:, 0]) # : seria para pegar todas as linhas e e o 0 seria para pegar a primeria coluna

# # linha 0 → [1, 2]
# linha 1 → [3, 4]
#            ↑
#         coluna 0   coluna 1


# 21. Explique o que é uma lista em Python e dê um exemplo.

# Uma lista em python e uma estrutura de dados que voce consegue armazenar diversos valores em uma unica variavel
# frutas = ["maca", "banan", "uva"]


# 22. Explique o que é um dicionário e como acessar seus valores.

# Um dicionario em python seria uma forma de voce armazenar um valor para uma chave e voce pode acessar seu valor quando voce pergunta pela chave do valor que voce esta procurando

# dados = {'nome': 'Eduardo'}
# print(dados['nome'])

# 23. Qual a diferença entre append() e insert()?

# No append o elemento adicionado vai sempre para o final da lista ja o append(valor)
#insert ele adiciona o elemente um uma pocisao espesifica insert(indice, valor)

# 24. Explique o que faz o método pop().

# O pop()Ele remove o conteudo dentro da lista do indice informado, caso o indice n for informado, sera removido o ultimo elemento dentro da lista
# e ele pode retornar o valor removido
# lista = [1, 2, 3]
# lista.pop(0)
# print(lista)

# O remove() remove o valor dentro da lista caso ele n exista da valluerError

# lista = [1, 2, 3]
# lista.remove(1)
# print(lista)

# O del e tipo um pop que pode deletar uma lista inteiro, mas ele n retorna o valor removido
# lista = [1, 2, 3]
# del lista[1]
# print(lista)

# 25. Qual a diferença entre dados['chave'] e dados.get('chave')?

#A diferenca esta quando o elemento n existe
# Quando voce usa dados['chave'] e ele n existe ele retorna um valor KeyError
#ja o dados.get('chave') caso ele n exista retorna um None

# 26. O que acontece ao acessar uma chave inexistente com colchetes?

# Ao voce acessar uma chave com colchetes e ela n existir ira retornar um erro de KeyError

# 27. Explique o que significa índice negativo em listas.

# Um indice negativo na lista significa que ele ir pegar os ultimos valores vai comecar pegando os ultimos valores da lista.

# 28. Qual a diferença entre for elemento in lista e for i in range(len(lista))?

# que no for elemento in lista ele vai pegar apenas os elementos que estao na lista, ele percorre os elementos da lista pega os valores
# No for i in range(len(lista)) ele nao vai pegar os valores mas o for vai rodar na mesma quantidadade de elementos que aquela lista tem pega os indices

# 29. Explique o que é uma matriz em Python.

# Uma matriz em python seria uma tabela composta por linhas e colunas, como uma planilha

# 30. O que é o NumPy e para que ele é usado?

# O NumPy e uma biblioteca em python usada para calcular vetores e matrizes de forma rapida e eficiente, ela calcula mais rapido do que uma lista normal

# lista = [1, 2, 3, 4, 5]
# print(sum(lista))

# 32. Crie um programa que conte quantos números pares existem em uma lista.

# lista = [1, 2, 3, 4, 5, 6]
# lista_pares = []

# for elemento in lista:
#     if elemento % 2 == 0:
#         lista_pares.append(elemento)
# print(len(lista_pares))

# 33. Crie um dicionário com 3 alunos e suas notas e exiba todas as notas.

# notas = {'aluno1': 9, 'aluno2': 10, 'aluno3': 7 }

# for nota in notas.values():
#     print(nota)

# 34. Solicite um número ao usuário e verifique se ele está em uma lista.

# lista = [1, 2, 3]
# numero = int(input("Digite um valor para ver se ele esta na lista: "))

# if numero in lista:
#     print(f"O numero {numero} esta na lista")

# else:
#     print(f"O numero {numero} nao esta na lista")

# 35. Crie uma lista e exiba apenas os valores maiores que 10.

# lista = [1, 3, 5, 10, 90, 20]

# for valor in lista:
#     if valor > 10:
#         print(valor)

# 36. Crie um dicionário e permita atualizar um valor.

# dados = {'idade': 17}
# change = int(input("Digite o novo valor: "))
# dados['idade'] = change
# print(dados)

# 37. Crie um programa que calcule a média de uma lista.

# lista = [1, 2, 3, 4]
# media = sum(lista) / len(lista)
# print(media)

# 38. Crie uma lista e remova todos os números negativos.

# lista = [-1, -2 , -3, 1, 2, 3]
# nova_lista = []

# for valor in lista:
#     if valor >= 0:
#         nova_lista.append(valor)

# print(nova_lista)

# 39. Solicite nomes e armazene em uma lista até digitar 'fim'.

# nomes = []

# print("Digite nomes para adicionar na lista para sair digite fim.")

# print()

# while True:
#     valor = input("Digite o nome: ")
#     if valor == "fim":
#         break
#     else:
#         nomes.append(valor)
#     print(nomes)

# 40. Crie um dicionário e verifique se uma chave existe.

# dados = {'nome': "gabriel", "idade": 18}

# chave = input("Digite uma chave para ver se ela esta no dicionario: ")


# if chave in dados:
#     print(f"A chave {chave} esta no dicionario")

# else:
#     print(f"A chave {chave} nao esta no dicionario")

# 41. Crie um programa que conte quantas vezes um número aparece em uma
# lista.

# lista = [1, 2, 3, 1, 3, 2]

# print(lista)
# ver = int(input("Fale o valor para ver quantas vezes o numero se repete: "))
# contar = lista.count(ver)
# print(f"O numero {ver} aparece {contar} vezes")


# 42. Crie um programa que encontre o maior valor em uma lista.

# lista = [1, 2, 3]

# print(max(lista))

# 43. Crie um dicionário de produtos e aplique desconto de 10%.

# produtos = {'monster': 9, 'coca-cola': 12}

# for produto in produtos:
#     produtos[produto] *= 0.90
# print(produtos)

# 44. Crie um programa que some apenas os números ímpares de uma lista.

# numero = [1, 2, 3, 4, 5]
# numero_impar = []

# for n in numero:
#     if n % 2 == 0:
#         None
#     else:
#         numero_impar.append(n)

# print(sum(numero_impar))

# 45. Crie uma lista e inverta seus elementos sem usar reverse().

# lista = [1, 2, 3, 4]
# inverta = lista[::-1]
# print(inverta)

# 46. Crie uma matriz 2x2 e exiba seus elementos.

# import numpy as np

# matriz = np.array([[1, 2],[3, 4]])
# print(matriz)

# 47. Some todos os elementos de uma matriz 2x2.

# import numpy as np

# matriz = np.array([[1, 2], [3, 4]])

# soma = 0

# for linha in matriz:
#     for valor in linha:
#         soma += valor

# print(soma)

# 48. Exiba apenas a diagonal principal de uma matriz 3x3.

# import numpy as np

# matriz = np.array([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])

# for i in range(3):
#     print(matriz[i][i])

# 49. Multiplique todos os elementos de uma matriz por 2.

# import numpy as np

# matriz = np.array([[1, 2], [3, 4]])
# print(matriz * 2)

# 49. Multiplique todos os elementos de uma matriz por 2.

# 50. Crie duas matrizes 2x2 e some seus valores (A + B).
# import numpy as np

# matriz1 = np.array([[1, 2], [3, 4]])
# matriz2 = np.array([[1, 2], [3, 4]])

# soma = matriz1 + matriz2
# print(soma)

# lista = ["hello", "world"]

# print(lista)

# lista = [1, 2, 3, 4 ,5]
# # print(sum(lista))
# lista_pares = []

# for elemento in lista:
#     if elemento % 2 == 0:
#         lista_pares.append(elemento)

# print(len(lista_pares))

# alunos = {'aluno1': 10, 'aluno2': 9, 'aluno3': 3}
# print(alunos['aluno1'])
# print(alunos['aluno2'])

# lista = [1, 2, 3]

# numero = int(input("Fale um numero para ver se ele esta na lista: "))

# if numero in lista:
#     print(f"O numero {numero} esta na lista")

# else:
#         print(f"O numero {numero} nao esta na lista")


# lista = [1, 2, 3, 10, 11, 12, 13]
# maior_10 = []


# for n in lista:
#     if n > 10:
#         maior_10.append(n)
# print(maior_10)

# dados = {'nome': 'Gabriel', 'idade': 18}
# chave = input("Qual chave voce deseja atualizar: ")
# valor = input("informe o novo valor da chave: ")
# dados[chave] = valor
# print(dados)

# lista = []
# print("informe o nome para ser adicionado na lista para sair digiete 'fim' ")

# while True:
#     nome = input("Digite o nome a ser informado: ")
#     if nome == 'fim':
#         break
#     else:
#         lista.append(nome)
# print(lista)

# lista = [1, 2, 3, 4, 1, 1]
# contar = lista.count(1)
# print(contar)

# lista = [1, 2, 3]
# print(f"O mairo valor da lista e {max(lista)}")

# produto = {'a': 10, 'b': 12}

# for produtos in produto:
#     produto[produtos] *= 0.90
# print(produto)

# lista = [1, 2, 3]
# inverter = lista[:: -1]
# print(inverter)


import numpy as np
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for i in range(3):
    print(matriz[i][i])

# melhoria na nova feature