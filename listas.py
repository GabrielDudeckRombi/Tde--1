import numpy as np

# 1. Crie uma lista com os números de 1 a 5 e imprima-a na tela.

# lista = [1, 2, 3, 4, 5]
# print(lista)

# 2. Dada a lista cores = ['vermelho', 'azul', 'verde', 'amarelo'], acesse e imprima a
# segunda cor da lista.

# lista_cores = ['vermelho', 'azul', 'verde', 'amarelo']

# print(lista_cores[1])

# 3. Adicione o número 10 ao final da lista numeros = [1, 2, 3].

# lista_numeros = [1, 2, 3]
# lista_numeros.append(10)
# print(lista_numeros)

# 4. Remova a palavra "banana" da lista frutas = ['maçã', 'banana', 'laranja'].

# lista_frutas = ['maçã', 'banana', 'laranja']
# lista_frutas.remove("banana")
# print(lista_frutas)

# 5. Encontre e imprima o tamanho (quantidade de elementos) da lista itens = [10,
# 20, 30, 40, 50].

# lista_itens = [10,20, 30, 40, 50]
# tamanho_lista = len(lista_itens)
# print(f"A lista tem {tamanho_lista} elementos.")

# 6. Verifique se o número 7 está presente na lista valores = [1, 3, 5, 7, 9] e
# imprima o resultado booleano.

# lista_valores = [1, 3, 5, 7, 9]

# resultado = 7 in lista_valores
# print(resultado)

# 7. Concatene as listas lista1 = [1, 2] e lista2 = [3, 4] em uma terceira lista.

# lista1 = [1, 2]

# lista2 = [3, 4]

# lista3 = lista1 + lista2
# print(lista3)

# 8. Inverta a ordem dos elementos da lista letras = ['a', 'b', 'c', 'd']

# lista_letras = ['a', 'b', 'c', 'd']

# lista_letras.reverse()
# print(lista_letras)

# 9. Conte quantas vezes o número 2 aparece na lista numeros = [1, 2, 2, 3, 2, 4].

# lista_numeros = [1, 2, 2, 3, 2, 4]

# quantidade = lista_numeros.count(2)

# print(quantidade)

# 10. Calcule e imprima a soma de todos os elementos da lista precos = [10.5,
# 20.0, 15.5].

# lista_precos = [10.5,20.0, 15.5]

# print(sum(lista_precos))

# 11. Escreva um programa que remova as duplicatas de uma lista, garantindo que
# a ordem original dos primeiros elementos encontrados seja mantida.

# lista_numeros = [1, 2, 2, 3, 2, 4]

# nova_lista = []

# for item in lista_numeros:
#     if item not in nova_lista:
#         nova_lista.append(item)

# print(nova_lista)

# 12. Encontre o maior e o menor número em uma lista de inteiros sem usar as
# funções nativas max() e min().

# lista = [10, 20]

# print(f"O maior numero da lista e {max(lista)}")
# print(f"O menor numero da lista e {min(lista)}")

# 13. Use list comprehension (compreensão de listas) para criar uma lista contendo
# os quadrados dos números de 1 a 10.

# quadrados = [x**2 for x in range(1, 11)]
# print(quadrados)

# 14. Dada uma lista mista de números, crie uma nova lista contendo apenas os
# números ímpares da lista original.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nova_lista = []

# for item in lista:
#     if item % 2 == 0:
#         None
#     else:
#         nova_lista.append(item)
# print(nova_lista)

# 15. Escreva um programa que rotacione os elementos de uma lista para a direita
# em n posições (Exemplo: a lista [1, 2, 3, 4, 5] com n=2 vira [4, 5, 1, 2, 3])

# lista = [1, 2, 3, 4, 5]
# n = 2

# n = n % len(lista)

# rotacione = lista[-n:] + lista[:-2]

# print(rotacione)

# 16. Dadas duas listas, encontre a interseção entre elas (os elementos que estão
# presentes em ambas) sem usar a conversão para conjuntos (set).

# lista1 = [1, 3, 7, 9, 6]

# lista2 = [3, 4, 1, 8, 2]

# intersecao = []

# for item in lista1:
#     if item in lista2 and item not in intersecao:
#         intersecao.append(item)

# print(intersecao)

# 17. "Achate" (flatten) uma lista de listas (uma matriz bidimensional) em uma única
# lista unidimensional (Exemplo: [[1, 2], [3, 4]] vira [1, 2, 3, 4]).

# matriz = np.array([[1, 2],
#                 [3, 4]])

# lista = matriz.flatten()

# print(lista)

# 18. Implemente o algoritmo de ordenação Merge Sort (Ordenação por Mistura)
# para ordenar uma lista desordenada de números em ordem crescente.

# lista = [4, 1, 3, 2]

# arrumar_lista = sorted(lista, reverse=False)

# print(arrumar_lista)

# def arrumar_lista(lista):
#     return  sorted(lista, reverse=False)

# lista = [4, 1, 3, 2]
# organizar = arrumar_lista(lista)
# print(organizar)

# 19. Dada uma lista de números inteiros (positivos e negativos), encontre a
# sublista contígua com a maior soma e retorne o valor dessa soma (Algoritmo
# de Kadane).

# lista = [1, -2, 3, -1, 2, -3]

# max_atual = lista[0]
# max_global = lista[0]

# for i in range(1, len(lista)):
#     max_atual = max(lista[i], max_atual + lista[i])
#     max_global = max(max_global, max_atual)

# print(max_global)

# 20. Escreva uma função recursiva que receba uma lista de números distintos e
# retorne todas as permutações possíveis de seus elementos.

def permutacao(lista):
    if len(lista) == 1:
        return [lista]
    
    resultado = []

    for i in range(len(lista)):
        elemento_atual = lista[i]

        restante = lista[:i] + lista[i+1:]

        for p in permutacao(restante):
            resultado.append([elemento_atual] + p)

    return resultado

lista = [1, 2 ,3]
resultado = permutacao(lista)

for p in resultado:
    print(p)