#Ex:1

# idade = int(input("Fale sua idade para votar: "))

# if idade >= 16:
#     voto = input("Em quem voce vai votar: ")
#     print(voto)

# else:
#     print("Infelizmente voce nao pode votar, voce nao tem idade suficiente")

# -----------------------------------------------------

# Ex: 2

# numero = int(input("Fale um numero inteiro: "))

# if numero > 0:
#     print(f"Esse {numero} numero e positivo")

# elif numero == 0:
#     print(f"Esse numero {numero} e Zero")

# else:
#     print(f"Esse numer {numero} e um valor negativo")

# ----------------------------------------

# Ex:3

# valor_compra = float(input("Digite o valor de um produto: "))

# if valor_compra > 100:
#     valor_compra = valor_compra * 0.9 
#     print(valor_compra)

# else:
#     print(f"O valor do seu produto {valor_compra} nao tem direito a desconto")

# --------------------------------------------------

# Ex: 4

# nota = float(input("Digite o valor da nota ela e de 0 a 10: "))

# if nota >= 9:
#     print("Parabéns!! Você foi aprovado!")

# elif 7 < nota <=8.9:
#     print("Aprovado!")

# elif 4 < nota <=6.9:
#     print("Em recuperacao")

# else:
#     print("Reprovado")

# Ex: 5

# numero = int(input("Fale o valor de um numero inteiro: "))

# if numero % 2 == 0:
#     print(f"Esse numero e par {numero}")

# else:
#     print(f"Esse numero e impar {numero}")

#Ex 6:

# num_1 = float(input("Fale o valor do primeiro numero"))
# num_2 = float(input("Fale o valor do segundo numero"))

# print(f"Maior numero {max(num_1, num_2)}")
# print(f"Menor numero {min(num_1, num_2)}")

#Ex 7:

# usuario_correto = "admin"

# nome_usuario = input("Fale o nome do usuario: ")

# if usuario_correto == "admin":
#     print("Acesso concedido")

# else:
#     print("Usuário desconhecido")


#Ex 8:

# peso = int(input("Digite o seu peso: "))

# altura = float(input("Fale a sua altura:"))

# imc = peso / altura

# if imc > 25:
#     print(f"Acima do peso ideal kg:{peso}")

# else:
#     print(f"O seu peso esta normal kg:{peso}")

#Ex 9:

# print("Informe o valor dos 3 lados do triangulo:")

# lado_1 = float(input("Digite o valor de 1 lado:"))
# lado_2 = float(input("Digite o valor de 2 lado:"))
# lado_3 = float(input("Digite o valor de 3 lado:"))

# if lado_1 == lado_2 == lado_3:
#     print("Isso e um triangulo Equilátero")

# elif lado_1 != lado_2 != lado_3:
#     print("Isso e um triangulo Escaleno")

# else:
#     print("Isso e um triangulo Isósceles")

# Ex 10:

# num = int(input("Digite um valor de um numero inteiro: "))

# if num % 5 == 0:
#     print(f"O numero informado {num} e multiplo de 5 ")

# else:
#     print(f"O numero informado {num} e nao emultiplo de 5 ")

#Ex 11:

# idade = int(input("Informe sua idade: "))

# if idade >= 18:
#     print("Voce e adulto!")

# elif 14 <= idade <= 17:
#     print("Voce e juvenil B!")

# elif 11<= idade <= 13:
#     print("Voce e juvenil A!")

# elif 8<= idade <= 10:
#     print("Voce e Infantil B!")

# else:
#     print("Voce e Infantil A!")

# Ex 12:

# distancia = float(input("Informe a distancia que voce deseja percorrer em km: "))

# if distancia <= 200:
#     valor = distancia = 0.50
#     print(f"O valor que voce vai pagar e de: {valor}")

# else:
#     valor = distancia = 0.45
#     print(f"O valor que voce vai pagar e de: {valor}")

#Ex 13:

# ano = int(input("Digite um ano: "))

# if ano % 4 == 0:
#     print(f"O ano {ano} e bissexto")

# else:
#     print(f"O ano {ano} informado nao e bissexto")

#Ex 14:

# valor_salario = float(input("Fale o valor do salario: "))

# if valor_salario <= 1601:
#     valor_salario *= 1.15
#     print(f"O valor do seu salrio com os reajustes e igual a ${valor_salario}")

# else:
#     valor_salario *= 1.1
#     print(f"O valor do seu salario com os reajustes e igual a ${valor_salario}")

#Ex 15:

# velocidade = int(input("Informe a velocidade do carro em km: "))

# if velocidade > 80:
#     multa = velocidade - 80
#     valor_multa = multa * 7
#     print(f"Voce ultrapassou o limite de velocidade, voce tera que pagar ${valor_multa}")

# else:
#     print(f"A velocidade do carro km {velocidade} esta dentro do limite")

# Ex: 16:

# temperatura_celcius = float(input("Informe a temperatura em graus celcius: "))

# converter = input("Voce quer converter para Fahrenheit (F) ou Kelvin (K): ").upper()
# print(converter)

# if converter == "K":
#     c_k = temperatura_celcius + 273.15
#     print(f"A temperatura em celcius {temperatura_celcius} para Kelvin {c_k}")

# else:
#     c_f = (temperatura_celcius * 9/5) + 32
#     print(f"A temperatura em celcius {temperatura_celcius} para farenheit {c_f:.0f}")


# Ex 17:

# import math

# tamanha_pintar = int(input("Informe amanho em metros quadrados da área a ser pintada: "))

# if tamanha_pintar >= 54:
#     calcular = 18 * 3
#     quant_latas = math.ceil(tamanha_pintar / calcular )
#     quant_latas_preco = quant_latas * 80
#     print(f"Para voce pintar {tamanha_pintar}m vai precisar de mais de {quant_latas} e de ${quant_latas_preco}")

# else:
#     print(f"Voce vai precisar de 1 lata de tinta $80 para pintar {tamanha_pintar}m")

#Ex 18:


# valor_casa = float(input("Informe o valor da casa $: "))

# salario_comprador = float(input("Informe o seu salario $: "))

# anos = int(input("Informe em quantos anos voce quer pagar a casa: "))

# prestacao_casa = valor_casa / (anos  * 12)

# if prestacao_casa > salario_comprador * 0.3:
#     print("Emprstimo negado")

# else:
#     print("Emprestimo aprovado")


# cont = 0
# soma_medias = 0

# while cont < 3:
#     n1 = float(input("Digite a primeira nota: "))
#     n2 = float(input("Digite a segunda nota: "))
#     n3 = float(input("Digite a terceira nota: "))
#     n4 = float(input("Digite a quarta nota: "))

#     media = (n1 + n2 + n3 + n4) / 4
#     soma_medias += media
#     print("Media Anual: ", media)

#     if media >= 7:
#         print("Aprovado")
#     else:
#         print("Reprovado")

#     cont =+ 1
#     media_total = soma_medias / cont

# print(f"A media total e igual a {media_total:.2f}")

# acumular = 0
# contador = 0

# while True:
#     n = float(input("Digite um numero (se for negativo, o programa ira parar): "))

#     if n < 0:
#         break

#     if n % 2 == 0:
#         acumular += n
#         contador += 1 

# if contador > 0 :
#     media = acumular / contador
#     print(f"A soma dos numeros pares e: {acumular}")
#     print(f"A media dos numeros pares e: {media}")
# else:
#     print("Nenhum numero foi digitado")



