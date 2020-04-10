import time

while True:
	print('Convertendo valor em Fahrenheit')
	time.sleep(0.2)
	print("Aguarde...")
	time.sleep(1)
	celsius = int(input('Celcius: '))
	print()
	print()
	if celsius == 0:
		print("Ok!")
		time.sleep(2)
		print()
		print("Saindo do ºF...")
		print()
		break
	else:
		total = 9 * celsius / 5 + 32		#Calculo para a conversão
		print('O valor em ºF é: %dºF' % total)		#Print do resultado da conversão