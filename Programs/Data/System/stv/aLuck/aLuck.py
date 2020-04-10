from random import *
import time


#variável prêmio

escolhadousuario = int(input("Qual o valor do prêmio--> "))

premio = escolhadousuario
#inicialização do aLuck
time.sleep(2)
print("Escolha um número de 1 a 60")
time.sleep(0.2)
print("Não se esqueça! Boa Sorte!")
print("Valor do prêmio: {}".format(premio))
print()
print()
while True:
        sorteio1 = randrange(1, 60)
        aposta1 = int(input("Número: "))
        sorteio2 = randrange(1, 60)
        aposta2 = int(input("Número: "))
        sorteio3 = randrange(1, 60)
        aposta3 = int(input("Número: "))
        sorteio4 = randrange(1, 60)
        aposta4 = int(input("Número: "))
        sorteio5 = randrange(1, 60)
        aposta5 = int(input("Número: "))
        sorteio6 = randrange(1, 60)
        aposta6 = int(input("Número: "))
        if aposta1 and aposta2 and aposta3 and aposta4 and aposta5 and aposta6 == sorteio1 and sorteio2 and sorteio3 and sorteio4 and sorteio5 and sorteio6:
                print("RESULTADO: {} {} {} {} {} {}".format(sorteio1, sorteio2, sorteio3, sorteio4, sorteio5, sorteio6))
                print("")
                print("Você ganhou o sorteio! Parabéns!")
                print("Você jogou os números: {} {} {} {} {} {}".format(aposta1, aposta2, aposta3, aposta4, aposta5, aposta6))
                print()
        elif aposta1 and aposta2 and aposta3 and aposta4 and aposta5 and aposta6 != sorteio1 and sorteio2 and sorteio3 and sorteio4 and sorteio5 and sorteio6:
                print("Resultado:    {} {} {} {} {} {}".format(sorteio1, sorteio2, sorteio3, sorteio4, sorteio5, sorteio6))
                print("Você Jogou: {} {} {} {} {} {}".format(aposta1, aposta2, aposta3, aposta4, aposta5, aposta6))
