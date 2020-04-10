import time
import sys

#Variáveis do programa
textos = 0

iniciosy = input("--> ")


def linha():
	print("------------------------------------------------------------------")


while iniciosy == "addex":
	inicio = input("--> ")
	if inicio == "create text":
		print("Wait...")
		time.sleep(2)
		wtitulodream = input("Title--> ")
		linha()
		wtxtodream = input("Text--> ")
		linha()
		textos = textos + 1
		print("Ok.")
	elif inicio == "edit text":
		print("Wait...")
		time.sleep(2)
		if textos == 0:
			print("Text not found. Please type 'help' for more informations")
		else:
			wtituloeditdream = input("Title edit--> ")
			wtextoeditdream = input("Text edit--> ")
			print("Editing text...")
			wtextoeditdream = wtextodream
			time.sleep(1)
			print("Editing title...")
			wtituloeditdream = wtitulodream
			time.sleep(1)
			print("Ok.")
	elif inicio == "opentext":
		print("Wait...")
		if textos == 1:
			print("We find {} text".format(textos))
			lista = [wtitulodream]
			lista2 = [wtextodream]
			linha()
			print(lista)
			linha()
			print(lista2)
		else:
			print("We don't find texts. Please create a text to appears here!")
	else:
		print("Error 010")
		linha()
		print("Please, type 'help' for more informations")
while iniciosy != "addex":
	print("ERROR")
	time.sleep(2)
	print("close program...")
	linha()
	break
	print("Off...")
	break
	quit()