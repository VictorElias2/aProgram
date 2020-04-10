import time
import random

NumeroAleatorioModel = random.randint(000,999)


listaInt = []
listaFloat = []
listaStr = []

nomeUsuario = input("Qual é o seu nome? ")

print("Olá, %s! Bem-vindo ao aList." % (nomeUsuario))
print("Nesse programa poderá criar listas com números e textos.")
print("Poderá usar esse programa para listas de mercado, lista de funcionarios, trabalhos, e outros.")
print("Digite /help para mais informações")
print("Aguarde...")
time.sleep(2)
print("Pronto!")
print()

while True:
    perLista = input("Função--> ")

    if perLista == "/create item int" or perLista == "/create i":
        #cria a lista de números inteiros
        try:        
            perItemInt = int(input("Item--> "))
            listaInt.append(perItemInt)
            print("Criado!")
        except ValueError:
            print("Somente número são permitidos nessa função.")
    elif perLista == "/create item float":
        #cria a lista de números quebrados
        try:
            perItemFloat = float(input("Item--> "))
            listaFloat.append(perItemFloat)
            print("Criado!")
        except ValueError:
            print("Somente número fracionarios são permitidos nessa função.")
    elif perLista == "/create item text":
        #cria a lista de texto
        perItemStr = input("Item--> ")
        if perItemStr == "" or perItemStr == " ":
            print("Error, try again...")
            print()
        else:
            listaStr.append(perItemStr)
            print("Criado!")
            print()
    elif perLista == "/del":
        #opção de deletar algum objeto da lista
        print("Error1")
        print()
    elif perLista == "/open list n" or perLista == "/open list number":
        print("Abrindo lista...")
        time.sleep(2)
        print(listaInt)
    elif perLista == "/about":
        print("Model: {}".format(NumeroAleatorioModel))
        print("Username: {}".format(nomeUsuario))
        print("Year: 2020")
        print()
    elif perLista == "/help":
        print("Error2")
        print()
        #cria a opção ajuda
    else:
        print("Comando inválido, digite /help para obter informação.")
        print()
