import ikea
import os
import time

#os.system('cls' if os.name == 'nt' else 'clear')

looping = True

#Möblernas egenskaper
Billy = ikea.ikea("Billy", "bokhylla", 599)
Skotterud = ikea.ikea("Skotterud", "resårbotten", 4295)
Hilja = ikea.ikea("Hilja", "Gardiner", 249)
Stoense = ikea.ikea("Stoense", "Matta", 1895)
Bestå = ikea.ikea("Bestå", "TV-bänk", 2195)
Malm = ikea.ikea("Malm", "Sängstomme", 2795)

#Lista av möbler
list = [Billy, Skotterud, Hilja, Stoense, Bestå, Malm]

#Intro, Frågar om mängd pengar
print()
print("Välkommen till IKEA") 
print()
time.sleep(1)
print("Hur mycket kronor innehavar ni?")
saldo = int(input("Kr: "))
print()
print("OK")
time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')

#for ikea in list:
#    print(ikea.price)


while looping:
    
    #Välja om programmet ska visa möbler, visa saldo eller avsluta
    print()
    print("IKEA")
    print()
    print("(1) Lista av Möbler")
    print("(2) Visa ditt saldo")
    print("(3) Jag har inge mer peng :(")
    print("(4) Avsluta")
    choice = input("Val: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    #Visar möbler i nummerordning, samt att man får välja vilken man går in på
    if choice == "1":
        print("Möbler")

        i=0

        for ikea in list:
            print("(" + str(i+1) + ") " + ikea.name)
            i=i +1


        schoice = input("Val: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        #Visar billy
        if schoice == "1":
            print(Billy.name)
            print(Billy.category)
            print(str(Billy.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            bchoice = input("j/n: ")
            os.system('cls' if os.name == 'nt' else 'clear')

            if bchoice == "j":
                #Köper produkten om du har tillräckligt med pengar
                if saldo > Billy.price:
                    print("Du bra val, " + Billy.name + " köpad")
                    saldo = saldo - Billy.price
                    print("Du innehavar nu " + str(saldo) + " kr.")
                #Inte tillräckligt med pengar
                else:
                    print("Jävla fattiglapp, gå tillbaka till ditt hus oh wait du har inget.")
                    print()
                    time.sleep(4)
                    print("No money having ass")
                    time.sleep(2)
            elif bchoice == "n":
                #Frågar om du vill restarta, stänger av programmet om nej
                print("Fuck you")
                print("restart")
                restart = input("j/n: ")
                if restart == "j":
                    print("good")
                else:
                    print()
                    time.sleep(2)
                    print("...Go then")
                    print()
                    time.sleep(2)
                    break
            else:
                print("Invalid")

        #Visar Skotterud
        elif schoice == "2":
            print(Skotterud.name)
            print(Skotterud.category)
            print(str(Skotterud.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            skchoice = input("j/n: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if skchoice == "j":
                if saldo > Skotterud.price:
                    print("Du bra val, " + Skotterud.name + " köpad")
                    saldo = saldo - Skotterud.price
                    print("Du innehavar nu " + str(saldo) + " kr.")
                else:
                    print("Jävla fattiglapp, gå tillbaka till ditt hus oh wait du har inget.")
                    print()
                    time.sleep(5)
                    print("No money having ass")
                    time.sleep(3)
            elif skchoice == "n":
                print("Fuck you")
                print("restart")
                restart = input("j/n: ")
                if restart == "j":
                    print("good")
                else:
                    print()
                    time.sleep(2)
                    print("...Go then")
                    print()
                    time.sleep(2)
                    break
            else:
                print("Invalid")
        
        #Visar Hilja
        elif schoice == "3":
            print(Hilja.name)
            print(Hilja.category)
            print(str(Hilja.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            Hchoice = input("j/n: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if Hchoice == "j":
                if saldo > Hilja.price:
                    print("Du bra val, " + Hilja.name + " köpad")
                    saldo = saldo - Hilja.price
                    print("Du innehavar nu " + str(saldo) + " kr.")
                else:
                    print("Jävla fattiglapp, gå tillbaka till ditt hus oh wait du har inget.")
                    print()
                    time.sleep(5)
                    print("No money having ass")
                    print()
                    time.sleep(3)
            elif Hchoice == "n":
                print("Fuck you")
                print("restart?")
                restart = input("j/n: ")
                if restart == "j":
                    print("good")
                else:
                    print()
                    time.sleep(2)
                    print("...Go then")
                    print()
                    time.sleep(2)
                    break
            else:
                print("Invalid")
        
        #Visar Stoense
        elif schoice == "4":
            print(Stoense.name)
            print(Stoense.category)
            print(str(Stoense.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            stchoice = input("j/n: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if stchoice == "j":
                if saldo > Stoense.price:
                    print("Du bra val, " + Stoense.name + " köpad")
                    saldo = saldo - Stoense.price
                    print("Du innehavar nu " + str(saldo) + " kr.")
                else:
                    print("Jävla fattiglapp, gå tillbaka till ditt hus oh wait du har inget.")
                    print()
                    time.sleep(5)
                    print("No money having ass")
                    time.sleep(3)
            elif stchoice == "n":
                print("Fuck you")
                print("restart")
                restart = input("j/n: ")
                if restart == "j":
                    print("good")
                else:
                    print()
                    time.sleep(2)
                    print("...Go then")
                    print()
                    time.sleep(2)
                    break
            else:
                print("Invalid")

        #Visar Bestå
        elif schoice == "5":
            print(Bestå.name)
            print(Bestå.category)
            print(str(Bestå.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            bechoice = input("j/n: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if bechoice == "j":
                if saldo > Bestå.price:
                    print("Du bra val, " + Bestå.name + " köpad")
                    saldo = saldo - Bestå.price
                    print("Du innehavar nu " + str(saldo) + " kr.")
                else:
                    print("Jävla fattiglapp, gå tillbaka till ditt hus oh wait du har inget.")
                    print()
                    time.sleep(5)
                    print("No money having ass")
                    time.sleep(3)
            elif bechoice == "n":
                print("Fuck you")
                print("restart")
                restart = input("j/n: ")
                if restart == "j":
                    print("good")
                else:
                    print()
                    time.sleep(2)
                    print("...Go then")
                    print()
                    time.sleep(2)
                    break
            else:
                print("Invalid")
        #Visar malm, 
        elif schoice == "6":
            print(Malm.name)
            print(Malm.category)
            print(str(Malm.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            mchoice = input("j/n: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if mchoice == "j":
                if saldo > Malm.price:
                    print("Du bra val, " + Malm.name + " köpad")
                    saldo = saldo - Malm.price
                    print("Du innehavar nu " + str(saldo) + " kr.")
                else:
                    print("Jävla fattiglapp, gå tillbaka till ditt hus oh wait du har inget.")
                    print()
                    time.sleep(5)
                    print("No money having ass")
                    time.sleep(3)
            elif mchoice == "n":
                print("Fuck you")
                print("restart")
                restart = input("j/n: ")
                if restart == "j":
                    print("good")
                else:
                    print()
                    time.sleep(2)
                    print("...Go then")
                    print()
                    time.sleep(2)
                    break
            else:
                print("Invalid")


    #Visar saldo
    elif choice == "2":
        print()
        print("Du har " + str(saldo) + " kr kvar")
        print()
    
    #Hjälp om man har slut på pengar
    elif choice == "3":
        print()
        print("Fattig?")
        tigga = input("j/n: ")
        if tigga == "j":
            print()
            print("Sämst")
            print()
            time.sleep(1)
            print("Vill du ha hjälp eller?")
            print()
            print("Du behöver bara göra en snabb quiz för att få igen lite kosing")
            print()
            time.sleep(2.5)
            print("Vill du göra quizen?")
            hjälp = input("j/n: ")
            if hjälp == "j":
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("Då börjar vi!")
                print("Fråga 1: ")
                print("7 + 7 = ?")
                print()
                print("(1): 14")
                print("(2): 77")
                print("(3): 12")
                Svar1 = input("Svar: ")
                if Svar1 == "3":
                    print()
                    print("Correct!!")
                    time.sleep(2.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print()
                    print("Fråga 2: ")
                    print("7 - 7 = ?")
                    print()
                    print("(1): 12")
                    print("(2): 0")
                    print("(3): -14")
                    Svar2 = input("Svar: ")

                    if Svar2 == "1":
                        print()
                        print("Correct!!")
                        time.sleep(2.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print()
                        print("Fråga 3: ")
                        print("Vad tycker du om banan och curry på pizza?")
                        print("(1): Det smakar bra!")
                        print("(2): Det är inte något speciellt")
                        print("(3): Det hör hämma i helvetet")
                        Svar3 = input("Svar: ")

                        if Svar3 == "3":
                            print()
                            print("Correct!!")
                            time.sleep(2.5)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print()
                            print("Fråga 4: ")
                            print("vad är dina åsikter om blåbärspaj?")
                            print("(1): Det funkar sisådär")
                            print("(2): Det är en av de sämsta pajerna")
                            print("(3): Det är utan tvekan den bästa pajen")
                            Svar4 = input("Svar: ")

                            if Svar4 == "3":
                                print()
                                print("Correct!!")
                                time.sleep(2.5)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print()
                                print("Väldigt imponerande, du har klarat quizen")
                                print()
                                time.sleep(2)
                                print("Som pris får du 6000 kr in i ditt bankkonto")
                                saldo = saldo + 6000
                                print("Saldo: " + str(saldo))
                                time.sleep(2)

                            elif Svar4 == "2":
                                print()
                                print("Skaffa nya smaklökar")
                                print()
                                print("Du förtjänar inte att vara här, hejdå")
                                time.sleep(2)
                                break

                            else:
                                print("False")

                        elif Svar3 == "1":
                            print()
                            print("vad fan är det för fel på dig")
                            print()
                            print("Nej du ska bort härifrån, försvinn")
                            time.sleep(2)
                            break

                        else:
                            print("False")
                    else:
                        print("False")
                else:
                    print("False")
                    

            elif hjälp == "n":
                print()
                print("...")
                print()
                time.sleep(1)
                print("Stay broke then")
                time.sleep(1)
                print("Bitch")
                time.sleep(1)

        elif tigga == "n":
            print()
            print("...")
            time.sleep(1.5)
            print("Jaha, tillbaka då")

        else:
            print()
            print("vad snackar du i?")
            print()

    elif choice == "4":
        looping = False

    else:
        print("Sug mina bollar")