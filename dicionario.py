# 1. Crie um dicionário com nome, idade e cidade de uma pessoa.
# Solicite ao usuário uma chave e exiba o valor correspondente

# pessoa = {"nome": "gabriel", "idade": 18, "cidade": "curitiba"}

# chave = input("Digite a chave correta ['nome', 'idade', 'cidade']")

# if chave in pessoa:
#     print(pessoa)

# else:
#     print("Os valores colocados nao corresponde com o da pessoa!")

# ------------------------------------------------------------------------

# Crie um dicionário com o preço de três produtos. Peça ao usuário
# qual produto deseja alterar e o novo preço. Atualize o dicionário e
# exiba o resultado.

# produto = {"coca-cola": 10, "macarrao": 15, "monster": 9}

# chave = input("Qual produto voce deseja atualizar o preco : ").lower().strip()
# produto
# if chave in produto:
#     novo_valor = float(input("Digite o novo valor do produto: "))

#     produto[chave] = novo_valor
#     print(f"Dicionario Atualizado! {produto}")

# ------------------------------------------------------------------

# Crie um dicionário vazio. Solicite ao usuário um nome e uma idade
# e armazene essas informações no dicionário como chave e valor.
# Exiba o dicionário ao final.

# pessoa = {}

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# pessoa[nome] = idade

# print(pessoa)

# --------------------------------------------------------------
# Peça ao usuário para informar três pares de dados (chave e valor).
# Utilize a função dict() para construir o dicionário e exiba o resultado.

# dicionario = dict()

# for i in range(3):
#     chave = input("Chave: ")
#     valor = input("Valor: ")
#     dicionario[chave] = valor

# print(dicionario)

#----------------------------------------------------------------------

# Crie um dicionário com alguns elementos. Pergunte ao usuário se
# deseja apagar todos os dados. Caso a resposta seja 'sim', utilize
# clear() e mostre o dicionário final

# dicionario = {"nome": "gabriel", "idade": 17, "cidade": "curitiba"}

# remover = input("Voce deseja remover todos os elementos da lista[SIM ou NAO]: ").lower()

# if remover == "sim":
#     dicionario.clear()
#     print(f"Novo dicionario{dicionario}")

# else:
#     print(dicionario)

#------------------------------------------------------------------------------

# Crie um dicionário com alguns dados. Faça uma cópia desse
# dicionário. Em seguida, altere um valor na cópia e mostre os dois
# dicionários para comparar

# dicionario = {"nome": "gabriel", "idade": 17, "cidade": "curitiba"}

# copia_dicionario = dicionario.copy()

# copia_dicionario["cidade"] =  "campo grande"

# print("Dicionario Original")
# print(dicionario)
# print()
# print("Dicioario Copiado")
# print(copia_dicionario)

#---------------------------------------------------------------------------

# Solicite ao usuário uma lista de nomes (separados por vírgula).
# Utilize fromkeys() para criar um dicionário onde todas as chaves
# sejam esses nomes e o valor padrão seja 0.

# nomes = input("Digite os nomes (separados por vírgula): ").split(",")

# dicionario = dict.fromkeys(nomes, 0)

# print(dicionario)

# Crie um dicionário com alguns alunos e suas notas. Peça ao
# usuário o nome de um aluno e utilize get() para buscar a nota. Caso
# o aluno não exista, exiba uma mensagem padrão.

# alunos = {"gabriel": 10, "Heitor": 8, "kosky": 7}

# nome = input("Informe o nome do aluno que voce deseja saber a nota: ").lower()

# nota = alunos.get(nome, "Aluno nao encontrado")

# print(nota)

# Crie um dicionário com produtos e preços. Mostre ao usuário todas
# as chaves, todos os valores e todos os pares chave–valor.

# produtos = {"coca-cola": 10, "macarrao": 15, "monster": 9}

# for chave in produtos.keys():
#     print(chave)

# for valor in produtos.values():
#     print(valor)

# for chave,valor in produtos.items():
#     print(f"{chave} -> R${valor}")

# --------------------------------------------

# Crie um dicionário com alguns dados. Peça ao usuário uma chave
# para remover usando pop(). Em seguida, remova um item com
# popitem(). Depois, peça novos dados ao usuário e atualize o
# dicionário com update(). Exiba o dicionário final.

# dados = {"nome": "gabriel", "idade": 18, "cidade": "curitiba"}

# print(dados)

# remov_chave = input("Digite a chave que voce deseja retirar: ")

# if remov_chave in dados:
#     dados.pop(remov_chave)
#     print("Chave removida! ", dados)

# else:
#     print("Chave nao encontrada! ")

# nova_chave = input("Digite uma nova chave: ")
# novo_valor = input("Digite um valor novo: ")

# dados.update({nova_chave: novo_valor})

# print("Novo valor adicionado!", dados)

# --------------------------------------------------------

# Desenvolva um programa em Python que simule um pequeno
# sistema de gerenciamento de usuários utilizando dicionários.
# O sistema deve iniciar com um dicionário previamente criado
# contendo pelo menos 3 usuários, onde a chave representa o nome do
# usuário e o valor representa sua idade.
# Ao iniciar, o programa deve exibir um menu de opções para o
# usuário, permitindo as seguintes operações:
# • Exibir todos os usuários cadastrados, mostrando:
# o apenas os nomes (utilizando keys()),
# o apenas as idades (utilizando values()),
# o e todos os pares nome–idade (utilizando items()).
# • Buscar um usuário pelo nome, utilizando o método get(). Caso o
# usuário não exista, o programa deve informar uma mensagem
# apropriada.
# Adicionar um novo usuário, solicitando nome e idade. A inserção
# deve ser feita diretamente no dicionário.
# • Atualizar a idade de um usuário existente, solicitando o nome e a
# nova idade.
# • Remover um usuário específico, utilizando o método pop().
# • Remover o último elemento inserido no dicionário, utilizando
# popitem().
# • Criar uma cópia do dicionário atual, utilizando copy(), e permitir que
# o usuário altere um dos valores na cópia, exibindo ao final tanto o
# dicionário original quanto a cópia para comparação.
# • Inicializar um novo dicionário com múltiplos usuários, utilizando
# fromkeys(), onde o usuário deve informar uma lista de nomes
# (separados por vírgula) e todos devem receber uma idade padrão
# definida pelo usuário.
# • Atualizar o dicionário principal com novos dados, utilizando
# update(), a partir de outro dicionário informado pelo usuário.
# • Limpar todos os dados do sistema, utilizando clear(), mediante
# confirmação do usuário.
# • Criar um novo dicionário utilizando a função dict(), a partir de uma
# lista de tuplas informadas pelo usuário.
# O programa deve continuar executando até que o usuário escolha a
# opção de sair.

usuarios = {"Gabriel": 17, "Vitor": 17, "Icaro": 25}

while True:
    print("\n===== MENU =====")
    print("1 - Exibir usuários")
    print("2 - Buscar usuário")
    print("3 - Adicionar usuário")
    print("4 - Atualizar idade")
    print("5 - Remover usuário (pop)")
    print("6 - Remover último (popitem)")
    print("7 - Copiar dicionário e alterar cópia")
    print("8 - Criar novo com fromkeys()")
    print("9 - Atualizar com update()")
    print("10 - Limpar dicionário (clear)")
    print("11 - Criar dicionário com dict()")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

# 1 - Exibir usuários
    if opcao == "1":
        print("\nNomes:", list(usuarios.keys()))
        print("Idades:", list(usuarios.values()))
        print("Nome-Idade:", list(usuarios.items()))

    # 2 - Buscar usuário
    elif opcao == "2":
        nome = input("Digite o nome: ")
        idade = usuarios.get(nome)
        if idade is not None:
            print(f"{nome} tem {idade} anos")
        else:
            print("Usuário não encontrado!")

    # 3 - Adicionar usuário
    elif opcao == "3":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        usuarios[nome] = idade
        print("Usuário adicionado!")

    # 4 - Atualizar idade
    elif opcao == "4":
        nome = input("Nome: ")
        if nome in usuarios:
            nova_idade = int(input("Nova idade: "))
            usuarios[nome] = nova_idade
            print("Idade atualizada!")
        else:
            print("Usuário não encontrado!")

    # 5 - Remover com pop()
    elif opcao == "5":
        nome = input("Nome para remover: ")
        if nome in usuarios:
            usuarios.pop(nome)
            print("Usuário removido!")
        else:
            print("Usuário não encontrado!")

    # 6 - Remover último com popitem()
    elif opcao == "6":
        if usuarios:
            removido = usuarios.popitem()
            print("Removido:", removido)
        else:
            print("Dicionário vazio!")

    # 7 - Copiar e alterar
    elif opcao == "7":
        copia = usuarios.copy()
        nome = input("Nome na cópia para alterar: ")
        if nome in copia:
            nova_idade = int(input("Nova idade na cópia: "))
            copia[nome] = nova_idade
        print("Original:", usuarios)
        print("Cópia:", copia)

    # 8 - fromkeys()
    elif opcao == "8":
        nomes = input("Digite nomes separados por vírgula: ").split(",")
        idade_padrao = int(input("Idade padrão: "))
        novo_dict = dict.fromkeys([n.strip() for n in nomes], idade_padrao)
        print("Novo dicionário:", novo_dict)

    # 9 - update()
    elif opcao == "9":
        novos = {}
        qtd = int(input("Quantos usuários deseja adicionar? "))
        for _ in range(qtd):
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            novos[nome] = idade
        usuarios.update(novos)
        print("Atualizado:", usuarios)

    # 10 - clear()
    elif opcao == "10":
        confirm = input("Tem certeza? (s/n): ")
        if confirm.lower() == "s":
            usuarios.clear()
            print("Dicionário limpo!")

    # 11 - dict() com tuplas
    elif opcao == "11":
        lista = []
        qtd = int(input("Quantos pares deseja inserir? "))
        for _ in range(qtd):
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            lista.append((nome, idade))
        novo_dict = dict(lista)
        print("Novo dicionário:", novo_dict)

    # 0 - sair
    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")

