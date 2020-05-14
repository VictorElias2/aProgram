#ATENTION -- ALL VARIABLES ARE IN PORTUGUESE(BRAZIL) AND I CAN'T CHANGE NOW. SORRY. ;)
#-------------------------------------------------------------------------------------

#Bibliotecas importadas
import time
import os
import math
import random

#Fuctions
def separador():
    print("-"*30)

def separadorLinha():
    print()
    print()
#Tamanho do Armazenamento do sistema
armazenamento = 2.00

#Começo do Sistema Operacional
#Variáveis do tipo de usuário
usertip = None

if armazenamento == 2.00:
    usertip = "DEV"
elif armazenamento == 4.00:
    usertip = "BASIC"
elif armazenamento == 8.00:
    usertip = "PREMIUM"
elif armazenamento == 10.00:
    usertip = "PRO"
elif armazenamento > 10.00:
    usertip = "GOLD"
else:
    time.sleep(2)
    print("Error")
    print("ERROR SYSTEM USERTIP")
    print()
    print()
    print("Exiting...")
    quit()

systemModel = random.randint(000, 999)

#Fim das variáveis do tipo de usuário

#Começo das variáveis globais
#Variaveis RandomNumber
tamanhoRandomNumber = 0.24
appRandomNumber = 0
versaoRandomNumber = 1.0
descricaoRandomNumber = "Generate random numbers in your choice."
randomNumbersList = []
#Variaveis do aSystem
tamanhoasystem = 0.34
descricaoasystem = "You will now be able to open some programs directly from aProgram"
appsystem = 0
#Fim das variaveis do aSystem

#Variaveis do ºF
appF = 0
tamanhoF = 0.6
descricaoF = "Convert Celcius to Fahrenheit!"
versaoF = 1.0
#Fim das variaveis do ºF

#Variáveis do aMédia
tamanhomedia = 0.09
appmedia = 0
descricaomedia = "Average your students and teachers in this fanatical program!"
versaoappmedia = 1.0
#fim das variáveis do aMédia

#Começo dos programas da loja
#Linguagem de programação
linguagemsys = "Python"

#começo DreamWorld
tamanhodream = 0.14
dream = 0
versaodream = 0.5
titulodream = 0
abertos = 0
descricaodream = "Create your texts, edit, save, and see later."
#Fim DreamWorld
#Fim dos programas da loja

#variaveis do sistema
linguagem = "Portugues(Brasil)"
tamanhosistema = 0.41
restart = " restart"
check = " check"
ready = " ready"
#Variáveis do Root do sistema
root = ["open sys", "open apps", "open store", "open about", "open help", "open tools", "open system", "open errors", "open infos", "open cal", "open * in system"]
rootoff = ["close sys", "close apps", "close store", "close about", "close help", "close tools", "close system", "close errors", "close infos", "close cal", "close * in system"]
#creatorsy
creator = "https://www.youtube.com/channel/UCFi3Y3LLWdIjqluPBwxSJMA?view_as=subscriber"

#versão, ferramentas, aplicativos e outros
engine = "aEngine"
versao = 1.1
aplicativos = ["cal", "store", "psc",]
ferramentas = len(aplicativos)
ano = 2020
#variaveis evento aProgram
eventos = 0
diaevento = 0
horasevento = "Nothing..."
sobreevento = "Nothing..."
#Fim das variáveis globais
#começo do sitema
armazenamento = armazenamento - tamanhosistema

time.sleep(1)
nome = input("Username: ")
if nome == "admin":
    erroInesperado = " :( THERE A PROBLEM WHEN STARTING THE SYSTEM"
    a = 1
    while True:
        a = a + 1000
        if a >= 5000:
            quit()
        print(a, erroInesperado)
        resolveerror = input("SYSTEM ERROR COMAND REPAIR--> ")
        if resolveerror == "off system":
            time.sleep(0.1)
            quit()
        elif resolveerror == "comand -system os- RESOLVE ERROR S paste systems/errors/comand/resolve/end is = True":
            time.sleep(2)
            print("WAIT 5 SECONDS")
            time.sleep(5)
            print("Error is FALSE")
            break
            time.sleep(2)
            print()
        elif resolveerror != "comand -system os- RESOLVE ERROR S paste systems/errors/comand/resolve/end is = True" and "off system":
            print()
            print("Comando errado, tente novamente.")
            print()
            print()
        else:
            print("TOTAL ERROR")
            print()
            time.sleep(3)
            quit()
elif nome == "":
    print("Erro")
    print()
    time.sleep(1)
    print("Exiting...")
    print("Logging out of {}".format(nome))
    time.sleep(0.1)
    print("Turning off...")
    time.sleep(0.5)
    quit()
elif nome == " ":
    print("Erro")
    print()
    time.sleep(1)
    print("Exiting...")
    print("Logging out of {}".format(nome))
    time.sleep(0.1)
    print("Turning off...")
    time.sleep(0.5)
    quit()
elif nome == "   ":
    print("Erro")
    print()
    time.sleep(1)
    print("Exiting...")
    print("Logging out of {}".format(nome))
    time.sleep(0.1)
    print("Turning off...")
    time.sleep(0.5)
    quit()
elif nome == None:
    print("Erro")
    print()
    time.sleep(1)
    print("Exiting...")
    print("Logging out of {}".format(nome))
    time.sleep(0.1)
    print("Turning off...")
    time.sleep(0.5)
    quit()
else:
    print()
    time.sleep(1)
    iniciosy = input("System: ")
    time.sleep(3)
    if iniciosy == "off":
        print("Logging out off {}".format(nome))
        time.sleep(2)
        print("Closing files...")
        time.sleep(0.1)
        print("Closing programs")
        time.sleep(0.1)
        print("Turning off...")
        time.sleep(2)
        quit()
    elif iniciosy == "about":
        print("aProgram {} - By Victor Elias".format(versao))
        print("System Language--> {}".format(linguagem))
        print("Username--> {}".format(nome))
        print("Version--> {}".format(versao))
        print("Model--> {}".format(systemModel))
        print("Engine--> {}".format(engine))
        print("Storage--> {}".format(armazenamento))
        print("Created in {}".format(linguagemsys))
    elif iniciosy == "flashoff":
        print("Logging out of {}\n Model--> {}".format(nome, systemModel))
        print("Turning off...")
        time.sleep(2.0)
        quit()
    else:
        print("Type the command 'help' for more information!")
        print()
        print()
        while iniciosy == "addex" or iniciosy == "start addex" or iniciosy == "start aProgram":
                inicio = input("--> ")
                if armazenamento == 0 or armazenamento < 0:
                    print("GLOBAL ERROR STORAGE")
                    print("PLEASE, CONTACT THE SUPORT IN THIS E-MAIL: aprogram@gmail.com")
                    time.sleep(5)
                    quit()
                elif inicio == "cal" or inicio == "calculator":
                    print("Opening calculator...")
                    time.sleep(2)
                    print()
                    wcal = input("cal-> ")
                    print()
                    if wcal == "mul" or wcal == "multiplier":
                        try:
                            n1 = int(input("Nº1: "))
                            n2 = int(input("Nº2: "))
                            total = n1 * n2
                            print()
                            print(total)
                            print()
                        except ValueError:
                            time.sleep(1)
                            print("This command is not valid.")
                    elif wcal == "div":
                        try:
                            n1 = int(input("Nº1: "))
                            n2 = int(input("Nº2: "))
                            if n2 == 0:
                                print("Erro")
                                time.sleep(0.2)
                                print()
                                print("Erro 040")
                                print()
                                print("For more information type 'help'")
                                print()
                                print()
                            elif n1 == 0 and n2 == 0:
                                print("Erro")
                                time.sleep(0.2)
                                print()
                                print("Erro 040")
                                print()
                                print("For more information type 'help'")
                                print()
                                print()
                            else:
                                total = n1 / n2
                                print()
                                print(total)
                                print()
                        except ValueError:
                            print("This command is not valid.")
                    elif wcal == "ad":
                        try:
                            n1 = int(input("Nº1: "))
                            n2 = int(input("Nº2: "))
                            total = n1 + n2
                            print()
                            print(total)
                            print()
                        except ValueError:
                            print("This command is not valid.")
                    elif wcal == "sub":
                        try:
                            n1 = int(input("Nº1: "))
                            n2 = int(input("Nº2: "))
                            total = n1 - n2
                            print()
                            print(total)
                            print()
                        except:
                            print("This command is not valid.")
                    elif wcal == "pi":
                        print()
                        print(math.pi)
                    elif wcal == "div pi":
                        try:
                            n1 = int(input("Number: "))
                            total = n1 / math.pi
                            print()
                            print(total)
                            print()
                        except ValueError:
                            print("This command is not valid.")
                    elif wcal == "mul pi":
                        try:
                            n1 = int(input("Number: "))
                            total = n1 * math.pi
                            print()
                            print(total)
                            print()
                        except ValueError:
                            print("This command is not valid")
                    elif wcal == "close" or wcal == "cancel":
                        print("Closing...")
                        time.sleep(0.5)
                        print("Ready.")
                        print()
                        print()
                    else:
                        print("Erro 050")
                        print()
                        print("For more information type 'help'")
                        print()
                        print()
                elif inicio == "off":
                    print("Fazendo logoff de {}".format(nome))
                    time.sleep(1)
                    print("Desligando...")
                    time.sleep(3)
                    quit()
                elif inicio == "psc":
                    note = input("Nota: ")
                    wp = int(input("How much time on screen?: "))
                    time.sleep(0.5)
                    print()
                    print(note)
                    print()
                    time.sleep(wp)
                    print() 
                    print() 
                    print("Time limit reached...")
                    print() 
                    print()
                elif inicio == "root system":
                    while True:
                        print("Restarting...")
                        time.sleep(6)
                        print(rootoff)
                        time.sleep(5)
                        print(root)
                        time.sleep(4)
                        print(check)
                        time.sleep(2)
                        print(ready)
                        time.sleep(3)
                        print(restart)
                        time.sleep(5)
                        print()
                        print()
                        break
                elif inicio == "uninstall aSystem" and appsystem == 1:
                    if appsystem == 0:
                        print("Sorry, we didn't find 'aSystem' in your tools.")
                        print()
                        print()
                    else:
                        print("Uninstalling...")
                        time.sleep(2)
                        appsystem = appsystem - 1
                        ferramentas = ferramentas - 1
                        armazenamento = armazenamento + tamanhoasystem
                        time.sleep(1) 
                        print("Successfully uninstalled!")
                elif inicio == "uninstall RandomNumber":
                    if appRandomNumber == 0:
                        print("Sorry, we didn't find 'RandomNumber' in your tools.")
                        print("Please, install in the store.")
                        separadorLinha() 
                    else:
                        print("Uninstalling...")
                        time.sleep(random.randint(2, 4))
                        appRandomNumber = appRandomNumber - 1
                        armazenamento = armazenamento + tamanhoRandomNumber
                        ferramentas = ferramentas - 1
                        aplicativos.remove("RandomNumber")
                elif inicio == "uninstall aDreamWorld" and dream == 1:
                    if dream == 0:
                        print("Sorry, we didn't find 'aDreamWorld' in your tools.")
                        print()
                        print()
                    else:
                        print("Uninstalling...")
                        time.sleep(2)
                        dream = dream - 1
                        armazenamento = armazenamento + tamanhodream
                        ferramentas = ferramentas - 1
                        titulodream = titulodream - 1
                        textosalvar = textosalvar - 1
                        abertos = abertos - 1            
                        print("Successfully uninstalled!")
                elif inicio == "uninstall Fahrenheit":
                    print("Uninstalling...")
                    time.sleep(3)
                    appF = appF - 1
                    ferramentas = ferramentas - 1
                    armazenamento = armazenamento + tamanhoF
                    print("Successfully uninstalled!")
                elif inicio == "uninstall aMédia" and appmedia == 1:
                    if appmedia == 0:
                        print("Sorry, we didn't find 'aMédia' in your tools.")
                        print()
                        print()
                    else:
                        print("Uninstalling...")
                        time.sleep(2)
                        appmedia = appmedia - 1
                        armazenamento = armazenamento + appmedia
                        ferramentas = ferramentas - 1
                        print("Successfully uninstalled!")          
                elif inicio == "con":
                    print("Open compatibility...")
                    time.sleep(4)
                    print("aProgram version-> {}".format(versao))
                    print("Developed by Victor Elias")
                    print("Command: Model {} Designed by Victor Elias".format(systemModel))
                    print("All rights reserved © 2020")
                    print("Username-> {}".format(nome))
                    time.sleep(10)
                elif inicio == "hour":
                    new = time.localtime()
                    if new.tm_hour == 1:
                        print("{} hour {} minutes {} seconds".format(new.tm_hour, new.tm_min, new.tm_sec))
                    else:
                        print("{} hours {} minutes {} seconds".format(new.tm_hour, new.tm_min, new.tm_sec))
                    print()
                    print()
                elif inicio == "date":
                    new = time.localtime()
                    if new.tm_mday == 00 or new.tm_mon == 00:
                        print("ERROR SYSTEM TIME")
                        time.sleep(2)
                        print("Closing... Try again later.")
                        print()
                        print()
                    else:
                        date = print("{}/{}/{}".format(new.tm_mday, new.tm_mon, new.tm_year))
                elif inicio == "config system":
                    print("Opening system configuration...")
                    time.sleep(2)
                    print("Seeking information...")
                    time.sleep(3)
                    print("name system")
                    print("storage details")
                    print()
                    time.sleep(2)
                    config = input("Config--> ")
                    if config == "change name":
                        print("Your username is-> '%s'" % nome)
                        mudanovo_nome = input("Nome-> ")
                        if mudanovo_nome == "":
                            print("Error")
                        elif mudanovo_nome == " ":
                            print("Error")
                        else:
                            time.sleep(0.2)
                            nome = mudanovo_nome
                            print("Ready!")
                    elif config == "search tools":
                        if len(aplicativos) >= 1:
                            print("Wait...")
                            time.sleep(2)
                            x = 0
                            while True:
                                per = input("Search program--> ")
                                time.sleep(0.3)
                                if aplicativos[x] == per:
                                    print("The {} exist! type open".format(aplicativos))
                                    break
                                else:
                                    print("This program does not exist! Please download new programs \n with the command 'store'!")
                                    break
                                x+=1
                        else:
                            print("Sorry, there are no tools.")
                            time.sleep(0.5)
                            print()
                            print()
                    elif config == "storage":
                        print("Aguarde...")
                        time.sleep(0.4)
                        print("Your Storage-> {}".format(armazenamento))
                        print("Your Total Storage-> {}".format(usertip))
                        print("Username-> {}".format(nome))
                        print("Aplications: \n{}".format(aplicativos))
                    elif config == "about engine":
                        print("The engine of system is: {}".format(engine))
                        print("Fully developed in {}".format(linguagemsys))
                    elif config == "cancel":
                        print("Close configurations...")
                        time.sleep(2)
                        print("Ready!")
                        print()
                        print()
                elif inicio == "break system":
                    print("...")
                    print("Exiting...")
                    time.sleep(0.1)
                    break
                elif inicio == "open aSystem" and appsystem == 1:
                    if appsystem == 0:
                        print("ERROR SYSTEM")
                        print("PROGRAM NOT FOUND")
                        print()
                        print()
                    else:
                        print("Abrindo...")
                        time.sleep(2)
                        wos = input("aSystem--> ")
                        if wos == "open os Google Chrome":
                            print("Opening Google Chrome...")
                            time.sleep(2)
                            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                            print()
                            print()
                        elif wos == "open os Notepad":
                            print("Opening notepad...")
                            time.sleep(2)
                            os.startfile("notepad.exe")
                            print()
                            print()
                        elif wos == "open os Internet Explorer":
                            print("Opening Internet Explorer...")
                            time.sleep(2)
                            os.startfile("C:\Program Files\internet explorer\iexplore.exe")
                            print()
                            print()
                        elif wos == "close app":
                            print()
                            print()
                elif inicio == "help":
                    print("Opening help...")
                    time.sleep(2)
                    print("Calculator:")
                    print("Command: cal")
                    print("Within 'cal' type:")
                    print("'mul' for multiplication / 'div' for division / 'ad' for addition / 'sub' for subtraction")
                    print()     #separação da calculadora
                    print("For time and date, just 'date' for date and 'hour' for hours.")
                    print("The 'con' code is for model compatibility and details.")
                    print("The code 'psc' is used to put a message on the screen and say how many seconds it will be exposed.")
                    print("The 'off' code just shuts down the system.")
                    print("The 'sys' code shows the user and the system.")
                    print("The flashoff code turns off the ultra-fast system.")
                    print("The 'store' code opens the system store.")
                    print("The 'tools' command show for you all programs that there in aProgram.")
                    print("The 'info system' code show informations of aProgram.")
                    print("The 'info user' code show informations of {}.".format(nome))
                    separador()
                    print("In 'store' type 'dir [name of program]' and appears the program informations.")
                    print("More information on the website:")
                    separador()
                    print()     #separação para os erros
                    print("Errors: ")
                    print("Error 010 - It is some wrong code or wrong character")
                    print("Error 020 - When 'addex' is typed in '->'")
                    print("Error 040 - When it is a divided number 0 (On the calculator)")
                    print("Error 050 - When typed incorrectly from the calculator")
                    print("Error 060 - When installed two or more programs")
                    print("Error 070 - Incorrect command in the aProgram store")
                    #print("In case of unknown errors please contact them through the email below:")
                    #print("aprogram@gmail.com")
                    separador()
                    print()
                    print()
                elif inicio == "dev info":
                    print("The creator of aProgram is Victor Elias")
                    print("Youtube Channel:")
                    print(creator)
                    separador()
                    print("Instagram: @victor_elias2")
                    sleep.time(4)
                    print()
                    print()
                elif inicio == "flashoff":
                    print("Ending programs...")
                    print("Logging out of {}".format(nome))
                    print("Turning off...")
                    quit()
                elif inicio == "event":
                    if eventos >= 1:
                        print("Victor Elias scored an event on the day {}".format(diaevento))
                        if horasevento == "Não sabe":
                            print("Hours: {}".format(horasevento))
                        else:
                            print("At {} o'clock".format(horasevento))
                            print("About: {}".format(sobreevento))
                            print()
                            print()
                            time.sleep(5)
                    else:
                        print("There are no events yet...")
                        time.sleep(3)
                elif inicio == "tools":
                    print("You have {} tools".format(ferramentas))
                    print("Your storage is %sMB" % (armazenamento))
                    print("Go to Store, you can download more tools ..")
                    print("Command--> store)")
                    print()
                    print("Your tools: ")
                    if ferramentas == 0:
                        print("GLOBAL ERROR")
                        time.sleep(0.2)
                        print("TOOLS IS 0")
                        print()
                        print()
                    if len(aplicativos) == 0:
                        print("Nonthing here.")
                        print("Install programs from the store by typing the command 'store'")
                        print()
                        print()
                    else:
                        print(aplicativos)
                    print()
                    print()
                elif inicio == "storage":
                    if armazenamento < 1.0:
                        time.sleep(1)
                        print("Your System have: {}M".format(armazenamento))
                        print("Your storage is full!")
                        print("Please, free up space to download more programs.")
                        print()
                        print()
                    else:
                        print("Wait...")
                        time.sleep(2)
                        print("Your storage: {}M".format(armazenamento))
                        print()
                        print()
                    #Começo da loja (store)
                elif inicio == "store":
                    if armazenamento < 1.00:
                        print("Sorry, your storage is out of space.")
                        print()
                        print()
                    else:
                        print("[aDreamWorld]")
                        time.sleep(0.1)
                        print("[aMédia]")
                        time.sleep(0.1)
                        print("[aSystem]")
                        time.sleep(0.1)
                        print("[ºF]")
                        time.sleep(0.1)
                        print("[RandomNumber]")
                        time.sleep(0.1)
                        print()
                        print("--Comming--")
                        time.sleep(0.1)
                        print("[Community]")
                        time.sleep(0.1)
                        print("More programs will be added soon")
                        time.sleep(0.1)
                        print()
                        winstalar = input("aStore--> ")
                        print()
                        if winstalar == "install aDreamWorld":
                            dream = dream + 1
                            if dream > 1:
                                print("Erro 060")
                                print()
                                print("Type 'help' for more informations")
                                print()
                                print()
                            else:
                                print("Downloading...")
                                time.sleep(5)
                                print("Installing...")
                                time.sleep(6)
                                print("Ready!")
                                armazenamento = armazenamento - tamanhodream
                                ferramentas = ferramentas + 1
                                aplicativos.append("aDreamWorld")   #Programa mostrado na tools
                        elif winstalar == "install F":
                            if appF > 1:
                                print("Error 060")
                                print()
                                print("Type 'help' for more information.")
                                print()
                                print()
                            else:
                                print("Downloading...")
                                time.sleep(4)
                                print("Installing...")
                                time.sleep(2)
                                print("Ready!")
                                armazenamento = armazenamento - tamanhoF
                                ferramentas = ferramentas + 1
                                appF = appF + 1
                                aplicativos.append("ºF")
                        elif winstalar == "install aMédia":
                            if appmedia > 1:
                                print("Error 060")
                                print()
                                print("Type 'help' for more informations")
                                print()
                                print()
                            else:
                                print("Downloading...")
                                time.sleep(7)
                                print("Installing...")
                                time.sleep(6)
                                print("Ready!")
                                appmedia = appmedia + 1
                                armazenamento = armazenamento - tamanhomedia
                                ferramentas = ferramentas + 1
                                aplicativos.append("aMédia")    #Programa mostrado na tools
                        elif winstalar == "install aSystem":
                            if appsystem > 1:
                                print("Error 060")
                                print()
                                print("Type 'help' for more informations")
                                print()
                                print()
                            else:
                                print("Downloading...")
                                time.sleep(15)
                                print("Installing...")
                                time.sleep(8)
                                print("Ready!")
                                ferramentas = ferramentas + 1
                                appsystem = appsystem + 1
                                armazenamento = armazenamento - tamanhoasystem 
                                aplicativos.append("aSystem")
                        #Instalação do app
                        elif winstalar == "install RandomNumber":
                            if appsystem > 1:
                                print("Error 060")
                                print()
                                print("Type 'help' for more informations")
                                print()
                                print()
                            else:
                                print("Downloading...")
                                time.sleep(3.4)
                                print("Installing...")
                                time.sleep(5.2)
                                print("Ready!")
                                ferramentas+=1
                                appRandomNumber+=1
                                armazenamento = armazenamento - tamanhoRandomNumber
                                aplicativos.append("RandomNumber")
                        elif winstalar == "dir RandomNumber":
                            print("Description: {}".format(descricaoRandomNumber))
                            print("Version: {}".format(versaoRandomNumber))
                            print("To donwload, please type 'install RandomNumber' in command of store")
                        elif winstalar == "dir aDreamWorld":
                            print("Description: {}".format(descricaodream))
                            print("Version: {}".format(versaodream))
                            print("To download, please type 'install aDreamWorld' in commando of store")
                            print()
                        elif winstalar == "dir aMédia":
                            print("Description: {}".format(descricaomedia))
                            print("Version: {}".format(versaoappmedia))
                            print("To download, please type 'install aMédia' in command of store.")
                            print()
                        elif winstalar == "dir F":
                            print("Description: {}".format(descricaoF))
                            print("Version: {}".format(versaoF))
                            print("To donwload, please type 'install F' in command of store")
                            print()
                        elif winstalar == "dir store":
                            print("Download programs to make your aProgram more attractive!")
                            print("Download programs created by the community!")
                            print("And be happy exploring the STORE!")
                            print("Want to submit your project? Send us an email!")
                            print("aprogram@gmail.com")
                            print()
                            print()
                        elif winstalar == "close app":
                            print()
                            print()
                        elif winstalar == "cancel":
                            print("Cancelled!")
                            print()
                            print()
                        elif winstalar == "close":
                            print()
                            print()
                        elif winstalar == "":
                            print("Erro 010")
                            print()
                            print("Type 'help' for more informations")
                            print()
                            print()
                        else:
                            print("Erro 070")
                            print()
                            print("For more informations, please type 'help'")
                            print()
                            print()
                            #Fim da loja
                elif inicio == "u-- install -v- sys- virusNumber":
                    r = 0
                    print("installing virus in system...")
                    time.sleep(2)
                    print("Broken")
                    while True:
                        r = r * 999599997999699899998999548568899145525884
                        print("This is NOT normal.")
                        print(r)
                        r+=1
                elif inicio == "open aMédia" and appmedia == 1:
                    print("Opening...")
                    time.sleep(2)
                    print()
                    print()
                    notas = [0,0,0,0,0]
                    soma = 0
                    x = 0
                    while x<5:
                        notas[x] = float(input("Note %d: " % x))
                        soma += notas[x]
                        x += 1
                    x = 0
                    while x<5:
                        print("Note %d: %6.2f" % (x, notas[x]))
                        x+=1
                    print("Média: %5.2f" % (soma/x))
                elif inicio == "open RandomNumber" and appRandomNumber == 1:
                    if appRandomNumber == 0:
                        print("ERROR")
                        print("PROGRAM NOT FOUND")
                        print()
                        print()
                    else:
                        tNumbersRandons = 0
                        print()
                        print("RandomNumber generates a random number of your choice.")
                        time.sleep(2)
                        qNumberRandons = int(input("How much numbers are you want?"))
                        randomNumber1 = int(input("Random Number Starts-> "))
                        randomNumber2 = int(input("Random Number Ends-> "))
                        if randomNumber1 > randomNumber2:
                            print("Sorry, but we find an error.")
                            print("Type in the 'Random Number Starts->' a number less 'Random Number Ends->'")
                        else:
                            while tNumbersRandons < qNumberRandons:
                                generateRandomNumber = random.randint(randomNumber1, randomNumber2)
                                randomNumbersList.append(generateRandomNumber)
                                tNumbersRandons += 1
                            if len(generateRandomNumber) > 1:
                                print("The random number is-> {}".format(generateRandomNumber))
                            else:
                                print("The randons numbers are-> {}".format(generateRandomNumber))
                elif inicio == "open aDreamWorld" and dream == 1:
                    if dream == 0:
                        print("ERROR")
                        print("PROGRAM NOT FOUND")
                        print()
                        print()
                    else:                    
                        print("Opening...")
                        time.sleep(3)
                        print()
                        print()
                        abertos = abertos + 1
                        wtitulodream = input("Title--> ")
                        titulodream = titulodream + 1
                        wnotadream = input("Text--> ")
                        print("Saving...")
                        time.sleep(2)
                        print("Ready!")
                        print()
                        print()
                elif inicio == "info aDreamWorld" and dream == 1:
                    print("Opening about aDreamWorld...")
                    time.sleep(3)
                    print()
                    print("Version: {}".format(versaodream))
                    print("Description: {}".format(descricaodream))
                elif inicio == "editext" and dream == 1:
                    if dream != 1:
                        print("Erro")
                        print()
                        print("PROGRAM NOT FOUND")
                        print()
                        print()
                    else:
                        print("Opening...")
                        time.sleep(2)
                        print()
                        ewtitulo = input("Edit title--> ")
                        wtitulodream = ewtitulo
                        print()
                        ewnotadream = input("Edit text--> ")
                        wnotadream = ewnotadream
                        print("Saving...")
                        time.sleep(1)
                        print("Ready!")
                        print()
                        print()
                elif inicio == "opentext" and dream == 1:
                    if dream == 1 and titulodream == 1:
                        time.sleep(2)
                        print("Opening text...")
                        time.sleep(2)
                        print("Text name--> {}".format(wtitulodream))
                        print("Text--> {}".format(wnotadream))
                        print()
                        print()
                    else:
                        print("Error")
                        print()
                        print("PROGRAM OR TEXT NOT FOUND")
                        print()
                        print()
                elif inicio == "dir opentext" and titulodream == 1 and dream == 1:
                    if titulodream == 1 and dream == 1:
                        time.sleep(3)
                        print("Opening...")
                        time.sleep(1)
                        print("We finded {} text".format(abertos))
                        time.sleep(2)
                        print("Loading...")
                        time.sleep(0.1)
                        print()
                        print(wtitulodream)
                        print()
                        print(wnotadream)
                        print()
                        print()
                    else:
                        print("You have no saved message, create one and it will appear here.")
                        time.sleep(1)
                        print()
                        print()
                elif inicio == "open F" and appF == 1:
                    if appF == 0:
                        print("ERROR")
                        print()
                        print("PROGRAM NOT FOUND")
                        print()
                        print()
                    else:
                        while True:
                            print("Warning!")
                            print("Enter 0 to exit")
                            print()
                            print('Converting value to Fahrenheit')
                            time.sleep(0.2)
                            print("Wait...")
                            time.sleep(1)
                            celsius = int(input('Celcius-> '))
                            print()
                            print()
                            if celsius == 0:
                                print("Ok!")
                                time.sleep(2)
                                print()
                                print("Leaving ºF...")
                                print()
                                time.sleep(0.1)
                                break
                                print()
                                print()
                            else:
                                total = 9 * celsius / 5 + 32        #Calculo para a conversão
                                print('The value in ºF is: %dºF' % total)      #Print do resultado da conversão
                elif inicio == "info user":         #informação do usuario
                    time.sleep(0.2)
                    print("Username-> {}".format(nome))
                    print("User tip-> {}".format(usertip))
                elif inicio == "info system":      #informação do sistema
                  print("Opening System...")
                  time.sleep(2)
                  print("Version: {}".format(versao))
                  print("Language: {}".format(linguagem))
                  print("User: {}".format(nome))
                  print("Created by language: {}".format(linguagemsys))
                  print()
                  print()
                elif inicio == "addex":
                    time.sleep(3)
                    print("Erro 020")
                    time.sleep(2)
                    print("COMAND SYSTEM")
                    print()
                    print()
                    #erro de código
                elif inicio == "copyright system":
                    print("Openinng copyright...")
                    time.sleep(2)
                    print("All rights reserved ₢ Victor Elias")
                    print("All types of system sales will automatically be banned from the site and the system")
                    print("The user is free to use the program but is limited")
                    print("Any type of code modified by the user will also be banned from the System")
                    print("Collaborate with all system and site usage rules")
                    print()
                    print()
                    #Botar o treco de notificação aqui!
                    #Mais tarde!
                elif inicio == "notifications":
                    print("Searching notifications...")
                    print("Sorry, this function is comming!")
                    time.sleep(2)
                elif inicio == "help programs":
                    print("Opening...")
                    time.sleep(2)
                    print("To install: ")
                    print("To install a program, you have to go on store and type:\n'install [program name]' wait for download and ready!")
                    separador()
                    print("To uninstall: ")
                    print("To uninstall a program, you have go to '-->' and type 'uninstall [program name]' wait for uninstall and ready!")
                    separador()
                    print("To see your programs: ")
                    print("For see your programs you have to go '-->' and type tools")
                    print()
                    print()
                elif inicio == "dir":
                  print("[calculator]")
                  time.sleep(0.1)
                  print("[psc]")
                  time.sleep(0.1)
                  print("[sys]")
                  time.sleep(0.1)
                  print("[alarm]")
                  time.sleep(0.1)
                  print("[date]")
                  time.sleep(0.1)
                  print("[hour]")
                  time.sleep(0.1)
                  print("[tools]")
                  time.sleep(0.1)
                  print("[config system]")
                  time.sleep(0.1)
                  print("[store]")
                  time.sleep(0.1)
                  print("[event]")
                  time.sleep(0.1)
                  print("[help]")
                  time.sleep(0.1)
                  print("[con]")
                  time.sleep(0.1)
                  print("[copyright]")
                  time.sleep(0.1)
                  print("[help]")
                  time.sleep(0.1)
                  print()
                  print()
                elif inicio == "":
                    print("Erro...")
                    print("Help? type 'help' for more informations")
                    print()
                    print()
                else:
                    print("Erro 010")
                    time.sleep(1)
                    print("Type 'help' for more informations")
                    print()
                    print()
        if iniciosy != "addex":
            print()
            print("GLOBAL ERROR")
            print()
            print()
            time.sleep(0.5)
            print("ADDEX COMAND NOT FOUND")
            print()
            time.sleep(0.7)
            print("Exiting...")
            time.sleep(1)
            print("Logging out of {}...".format(nome))
            time.sleep(3)
            print("Turning off...")
            time.sleep(1)
            quit()
        elif iniciosy == "":
            print("ERROR")
            print("PROGRAM SPACE ERROR")
            print()
            print("Exiting...")
            time.sleep(0.1)
            print("Logging out of {}".format(nome))
            time.sleep(2)
            print("Closing...")
            quit()
        else:
            print("ERROR")
            print("PROGRAM SPACE ERROR")
            print()
            print("Exiting...")
            time.sleep(0.1)
            print("Logging out of {}".format(nome))
            time.sleep(2)
            print("Closing...")
            quit()