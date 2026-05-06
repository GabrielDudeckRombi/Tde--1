# 1. Cadastro de números inteiros
# Crie um programa em Python que:
# • Solicite ao usuário a entrada de 10 números inteiros;
# • Armazene esses valores em uma lista chamada a.

# a = []

# for i in range(10):
#     numero = int(input(f"Digite um numero inteiro {i + 1}: "))
#     a.append(numero)
# print(a)

# 2. Exibição de elementos da a
# Considerando a a a do exercício anterior, crie um programa que:
# • Exiba todos os elementos da a na tela;
# • Mostre os valores um por linha.

# for i in a:
#     print(i)

# 3. Maior e menor valor
# Crie um programa em Python que:
# • Solicite ao usuário a entrada de 10 números inteiros;
# • Armazene esses valores em uma a chamada a;
# • Ao final, informe:
# • O maior valor da a;
# • O menor valor da a.


# a = []

# for i in range(10):
#     numero = int(input(f"Digite um numero inteiro {i + 1}: "))
#     a.append(numero)

# print(max(a))
# print(min(a))

# 4. Análise de notas de alunos
# Crie um programa em Python que:
# • Solicite ao usuário a quantidade de alunos da turma;
# • Em seguida, leia a nota de cada aluno (valores inteiros de 0 a
# 100);
# • Armazene as notas em uma lista;
# • Ao final, informe:
# • Quantos alunos estão abaixo da média;
# • Quantos alunos estão na média ou acima.
# Considere:
# • Média = 60.


# a = []
# acima = 0
# abaixo = 0
# alunos = int(input("Digite a quantidade de alunos da turma: "))

# for i in range(alunos):
#     nota = int(input(f"Digite a nota de cada aluno {i + 1}: "))
#     a.append(nota)


# print(a)
# for i in a:
#     if i >= 60:
#         acima  += 1
#     else:
#         abaixo += 1

# print(f"A quantidade de alunos acima da media e {acima}")
# print(f"A quantidade de alunos abaixo da media e {abaixo}")

# 5. Análise de números inteiros
# Crie um programa em Python que:
# • Solicite ao usuário a entrada de 5 números inteiros;
# • Armazene esses valores em uma lista;
# • Ao final, determine e exiba:
# • O maior número par da lista (caso exista);
# • O menor número ímpar da lista (caso exista);
# • O somatório de todos os elementos da lista;
# • A média dos valores.
# • Caso não existam números pares ou ímpares, exiba uma
# mensagem apropriada.

n = []

for i in range(5):
    numero = int(input(f"Digite 5 numeros inteiros {i + 1}:"))
    n.append(numero)

par = []
impar = []

for i in n:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

soma = sum(n)
media = soma / 5
print(f"A soma de todos os numeros = {soma}")
print(f"A media dos 5 numeros e = {media}")

if not par:
    print("A lista nao tem pares")
else: 
    print(f"O maior numero par da lista: {max(par)}")

if not impar:
    print("Nao tem impar")
else:
    print(f"O mair numero impar: {max(impar)}")

# 1) Construam um programa que registre o nome dos alunos de uma
# turma. A turma pode variar a quantidade de alunos. O programa
# deve ler a quantidade de alunos da turma e ler o nome de cada
# aluno e registrar e apresentar os nomes da lista na tela.

# lista_alunos = []
# alunos = int(input("Digite a quantidade de anos da sala: "))

# for i in range(alunos):
#     nomes = input(f"Digite o nome do {i + 1} aluno: ")
#     lista_alunos.append(nomes)

# for i in lista_alunos:
#     print(i)