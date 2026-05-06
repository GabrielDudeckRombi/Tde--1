# 1. Crie uma função somar(a, b) que retorne a soma de dois números.

# def somar(a, b):
#     return a + b

# resultado = somar(2, 8)
# print(resultado)

# 2. Crie uma função multiplicar(a, b) que retorne o resultado da multiplicação.

# def multiplicar(a, b):
#     return a * b

# resultado = multiplicar(2, 2)
# print(resultado)

# 3. Escreva uma função mensagem(nome) que imprima: Olá, <nome>!

# def saudacao(nome, mensagem ="Ola"):
#     print(f"{mensagem}, {nome}")

# saudacao("Ana")
# saudacao("Ana", "Oi")

# # 4. Crie uma função maior(a, b) que retorne o maior entre dois números.

# def maior_menor(a, b):
#     if a > b:
#         return a 

#     else:
#         return b

# resultado = maior_menor(4, 2)
# print(resultado)

# 5. Crie uma função dividir(a, b) que retorne o quociente e o resto da divisão.

# def dividir(a, b):
#     return a / b

# resultado = dividir(6, 2)

# print(resultado)

# 6. Crie uma função par_ou_impar(n) que retorne True se for par e False caso
# contrário.

# def par_ou_impar(n):
#     return n % 2 == 0

# resultado = par_ou_impar(3)

# print(resultado)

# 7. O que será exibido?
# def teste():
#   print('Olá')
# resultado = teste()
# print(resultado)

# Sera exibido Olá e None

# 8. Crie uma função apresentar(nome, idade, cidade) que imprima os dados
# formatados.

# def apresentar(nome, idade, cidade):
#     print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

# apresentar("Gabriel", 18, "Curitiba")

# # 9. Chame a função acima usando argumentos posicionais e nomeados.

# apresentar(nome="Gabriel", idade=18, cidade="Curitiba")

# # 10. O que acontece em: apresentar('Ana', 'Curitiba', 20)?

# apresentar('Ana', 'Curitiba', 20)

# Aparece Os elementos od dicionario Nome: Ana, Idade: 20,Cidade: Curitiba

# 11. Crie uma função saudacao(nome, periodo='dia').

# def saudacao(nome, periodo="dia"):
#     print(f"Bom {periodo}, {nome}")

# saudacao("Icaro")

# # 12. Modifique para aceitar valor padrão e valor informado.

# def saudacao(nome, periodo="dia"):
#     if periodo == "dia":
#         print(f"Bom dia, {nome}")

#     elif periodo == "tarde":
#         print(f"Boa {periodo}, {nome}")

#     elif periodo == "noite":
#         print(f"Boa {periodo}, {nome} ")

#     else:
#         print(f"Ola, {nome}")

# 13. Explique o erro em: def exemplo(a=1, b):

# O erro na funcao esta em b porque ele deveria vir na frente do a=1, o valor obrigatoria tem que vir no primeiro elemento ja no segundo vem os opcionais com um =

# 14. Crie uma função somar_todos(*numeros).

# def somar_todos(*numeros):
#     return sum(numeros)

# print(somar_todos(1, 2, 3))

# 15. Crie uma função mostrar_dados(**dados).

# def mostrar_dados(**dados):
#     for chave, valor in dados.items():
#         print(f"{chave}: {valor}")

# mostrar_dados(nome="Gabriel", idade=17, cidade="Curitiba")

# print(mostrar_dados)

# 16. Explique a diferença entre *args e **kwargs.

# *args recebe s valores posicionais como

# def exemplo(*args):
#     print(*args)

# exemplo(1, 2 ,3)

# O **kwargs recebe valores nomeados com:

# def exemplo(**kwargs):
#     print(kwargs)

# exemplo(nome="Gabriel", idade=17, cidade="Curitiba")

# 17. O que será exibido?
# x = 10
# def teste():
#   x = 5
#   print(x)
# teste()
# print(x)

# A saida sera 10 e 5 no primeiro print(x) sera o 5 e o print(x) que esta fora da funcao tera o valor 10

# 18. Corrija:
# contador = 0
# def incrementar():
#     contador += 1

# contador = 0

# def incrementar():
#     global contador
#     contador += 1

# incrementar()
# incrementar()
# print(contador)

# 19. Crie uma função triplo(x) e atribua a uma variável.

# def triplo(x):
#     return x * 3

# func = triplo

# print(func(5))

# 20. Crie executar(funcao, valor).

# def executar(funcao, valor):
#     return funcao(valor)


# def dobro(x):
#     return x * 2

# print(executar(dobro, 5))

# 21. Reescreva quadrado(x) usando lambda.

# quadrado = lambda x: x ** 2

# print(quadrado(4))

# 22. Use map para dobrar [1,2,3,4,5].

# def dobro(x):
#     return x * 2

# numeros = [1, 2, 3, 4, 5]

# resultado = map(dobro, numeros)
# print(list(resultado))

# 23. Use filter para pares.

# numeros = [1, 2, 3, 4, 5]

# def eh_par(x):
#     return x % 2 == 0

# pares = filter(eh_par, numeros)
# print(list(pares))

# 24. Crie uma função fatorial recursiva.

# def fatorial(n):
#     if n < 0: return None
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(fatorial(5))

# 25. Crie contagem recursiva de n até 0.

# def contagem(n):
#     if n < 0:
#         return None
#     print(n)
#     contagem(n - 1)

# contagem(100)

# 26. Explique o erro: def erro(n): return n * erro(n - 1)

# def erro(n):
#     return  n * erro(n - 1)

# O erro na funcao esta nela chamar ela mesma(recursao) mas ela nao tem uma codicao de parada, ent ela vai ficar rodando par sempre gerando um loop infinito

# 27. Crie função media(lista) com docstring.

# def media(lista):
#     """
#     No if ela checa se nao tem nada na lista se ela n tiver nada ela vai retornar 0
#     mas caso ela tenha o sum ira somar os valores da lista e vai dividir pela quantidade len
#     de numeros na lista.
#     """

#     if len(lista) == 0:
#         return 0
    
#     return sum(lista) / len(lista)

# print(media([10, 8, 7, 5]))


# 28. Use help() para exibir a documentação.

# def media(lista):
#     """
#     No if ela checa se nao tem nada na lista se ela n tiver nada ela vai retornar 0
#     mas caso ela tenha o sum ira somar os valores da lista e vai dividir pela quantidade len
#     de numeros na lista.
#     """

#     if len(lista) == 0:
#         return 0
    
#     return sum(lista) / len(lista)

# help(media)

# 29. Crie calculadora(a, b, operacao).

# def calcular(a, b, operacao):
#     if operacao == "soma":
#         return a + b
#     elif operacao == "subtracao":
#         return a - b
#     elif operacao == "multiplicacao":
#         return a * b
#     elif operacao == "divisao":
#         return a / b
#     else:
#         return "A operacao selecionada nao existe"

# print(calcular(10, 20, "divisao"))

# 30. Crie processar_dados(*args, **kwargs).

# def processar_dados(*args, **kwargs):
#     print("Valor posicionais (*args):")
#     for valor in args:
#         print(valor)

#     print("\nValor nomeados (**kwargs):")

#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")

# processar_dados(10, 20 ,30, nome="Gabriel", idade=17, cidade="Curitiba")