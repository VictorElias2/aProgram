#importações
import time
import sys

#variaveis
porcentagem = 100
iconpor = "%"

#Inicio do sistema
while True:
	inicio = input("--> ")
	while inicio == "int":
		time.sleep(2)
		print("aPersentage")
		print()
		time.sleep(1)
		por = int(input("Porcentagem: "))
		if por == "0":
			print("Erro")
			time.sleep(1)
			print()
			print()
		else:
			time.sleep(0.2)
			valor = int(input("Quantidade: "))
			if valor == "0":
				print("Erro")
				time.sleep(2)
				print()
				print()
			else:
				print("Calculando...")
				time.sleep(1)
				total = por * valor / porcentagem
				print(total{}).format(iconpor)
	while inicio == "exit":
		print("Saindo...")
		time.sleep(2)
		print("Fechando...")
		time.sleep(0.4)
		quit()
		break
	#Fim do sistema