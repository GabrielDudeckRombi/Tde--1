
lista =  {"nome": "heitor","sobrenome": "Rebechi Pere","altura": "1.89", "cep": "81630-170", "numero": "41988799758", "email": "heitorrebeki@gmail.com", "cpf": "107.484.389-47","irmao": "Felipe","namorada": "Maria fernanda", "amante": "Gabriel Raffaelli bolsonaro zanoni da silva","data de nascimento": "02d/02/2008", "idade": "18" , "casa": "Rua Irmã Flávia Borlet  Numero: 1121 ; Bairro: Hauer ; Cidade: Curitiba ; Estado: Paraná ; Sigla Estado: PR.", "melhor amigo": "Gabriel Raffaelli", "nome do pai do amigo": "Carlos Edu Ferrer", "com quem ele pega carona na faculdade": "Murilin", "numero do cartao": "14357767-321 cvv 381 vaidade 09/31","heitor e gay": "Sim","votou": " Sim ele votou no Bolsonaro mito 22 mestre", "o que ele estuda": "eng de software", "em qual faculdade": "PUC/PR", "comida favorita": "bife vegano zero cal no sugar zero gluten", "bebida favorita": "Cerveja / bebidas alcolicas  de cuido em geral", "sobremesa favorita": "morango do amor", "briquedo favorito": "labubu", "aura": "A quantidade de AURA dele = a 67 MANGO", "cor favorita": "Rosa do cu do raffaelli", "esporte favorito": "basquete", "nome do pai": "moacir jorge peres", "nome do sogro": "marcio", "nome da sobra": "edi" }

oq_voce_quer = input("Informe oque voce quer saber do heitor Rebechi Pere: ").lower()

if oq_voce_quer in lista:
    print(lista[oq_voce_quer])

else:
    print("Peca d nv oq vc quer!!!!!! 67 !!!!! perdeu AURA")


# bin_hex: dict = {"0000": "0", "0001": "1",
#                 "0010": "2", "0011": "3",
#                 "0100": "4", "0101": "5",
#                 "0110": "6", "0111": "7",
#                 "1000": "8", "1001": "9",
#                 "1010": "A", "1011": "B",
#                 "1100": "C", "1101": "D",
#                 "1110": "E", "1111": "F"}
 
# hex_bin: dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
#                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
 
# hex_dec: dict = {"0": 0, "1": 1, "2": 2, "3": 3,
#                 "4": 4, "5": 5, "6": 6,
#                 "7": 7, "8": 8, "9": 9,
#                 "A": 10, "B": 11, "C": 12,
#                 "D": 13, "E": 14, "F": 15}
 
# dec_hex: dict = {0: "0", 1: "1", 2: "2", 3: "3",
#                 4: "4", 5: "5", 6: "6", 7: "7",
#                 8: "8", 9: "9", 10: "A", 11: "B",
#                 12: "C", 13: "D", 14: "E", 15: "F"}
 
 
# def conferir_dec(num):
#    try:
#        num = int(num)
#    except ValueError:
#        return False
#    return str(num).isdigit()
 
# def conferir_bin(num):
#    for n in num:
#        if n != "1" and n != "0":
#            return False
#    return True
 
# def conferir_hex(num):
#    for x in num:
#        if x not in bin_hex.values():
#            return False
#    return True
 
 
# def conv_dec(num, num_type):
#    if num_type == "b":
#        list_bin = []
#        for n in range(len(num)):
#            list_bin.append(n)
#        reversed_list_bin = list_bin.copy()
#        reversed_list_bin.reverse()
 
#        resultado = 0
#        index_count = 0
#        for i in reversed_list_bin:
#            resultado += (int(num[list_bin[index_count]]) * (2 ** i))
#            index_count += 1
#        return resultado
 
#    if num_type == "h":
#        list_hex = []
#        for n in range(len(num)):
#            list_hex.append(n)
#        reversed_list_hex = list_hex.copy()
#        reversed_list_hex.reverse()
 
#        char_hex = []
#        for char in num:
#            char_hex.append(char)
 
#        resultado = 0
#        index_count = 0
#        for i in reversed_list_hex:
#            resultado += hex_dec[char_hex[index_count]] * (16 ** i)
#            index_count += 1
#        return resultado
 
# def conv_bin(num, num_type):
#    if num_type == "d":
#        num = int(num)
#        num_bin = ""
#        while num > 1:
#            if num % 2 != 0:
#                num_bin += "1"
#            else:
#                num_bin += "0"
#            num = num // 2
#        num_bin += "1"
#        return num_bin[::-1]
 
#    if num_type == "h":
#        num_bin = ""
#        for c in num:
#            num_bin += hex_bin[c]
#        return num_bin
 
# def conv_hex(num, num_type):
#    if num_type == "d":
#        num = int(num)
#        num_hex = ""
#        while num > 0:
#            resto = num % 16
#            num_hex += dec_hex[resto]
#            num = num // 16
#        return num_hex[::-1]
 
#    if num_type == "b":
#        while len(num) % 4 != 0:
#            num = "0" + num
#        num_hex = ""
#        num_bin = ""
#        index_bin = 0
#        for x in range(len(num) // 4):
#            for y in range(4):
#                num_bin += num[index_bin]
#                index_bin += 1
#            num_hex += bin_hex[num_bin]
#            num_bin = ""
#        return num_hex
 
 
# while True:
#    num = input("Digite o número que deseja converter (Digite 'Q' para sair): ").upper()
#    if num == "Q":
#        break
#    num_type = input("Esse número está em que sistema? (d / b / h): ").lower()
#    if num_type == "d":
#        if not conferir_dec(num=num):
#            print("Resposta Inválida")
#            continue
#    elif num_type == "b":
#        if not conferir_bin(num=num):
#            print("Resposta Inválida")
#            continue
#    elif num_type == "h":
#        if not conferir_hex(num=num):
#            print("Resposta Inválida")
#            continue
#    else:
#        print("Resposta Inválida")
#        continue
 
#    while True:
#        conversao: str = input("Deseja converter para qual sistema de numeração (d / b / h): ").lower()
#        if conversao == num_type:
#            print("Não é possível converter um sistema para ele mesmo")
#        elif conversao == "d":
#            print(f"{num}({num_type}) -> ({conversao}) = {conv_dec(num, num_type)}")
#            break
#        elif conversao == "b":
#            print(f"{num}({num_type}) -> ({conversao}) = {conv_bin(num, num_type)}")
#            break
#        elif conversao == "h":
#            print(f"{num}({num_type}) -> ({conversao}) = {conv_hex(num, num_type)}")
#            break
#        else:
#            print("Resposta Inválida")
 
# # Codigo feito 100% pela inteligenia artifical! 

# exercicio adicional heitor
