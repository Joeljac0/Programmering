import ikea
import os
import time

looping = True

Billy = ikea.ikea("Billy", "bokhylla", 599)
Skotterud = ikea.ikea("Skotterud", "resårbotten", 4295)


list = [Billy, Skotterud]
saldo = 5000
#for ikea in list:
#    print(ikea.price)

while looping:
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("(1) Lista av Möbler")
    print("(2) Visa ditt saldo")
    print("(3) Avsluta")
    choice = input("Val: ")
    if choice == "1":
        print("Möbler")

        i=0

        for ikea in list:
            print("(" + str(i+1) + ") " + ikea.name)
            i=i +1


        schoice = input("Val: ")

        if schoice == "1":
            print(Billy.name)
            print(Billy.category)
            print(str(Billy.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            bchoice = input("j/n: ")
            if bchoice == "j":
                if saldo > Billy.price:
                    print("Du bra val, " + Billy.name + " köpad")
                    saldo = saldo - Billy.price
                    print("Du innehavar nu " + str(saldo) + " peng.")
                else:
                    print("Jävla fattiglapp, gå tillbaka till ditt hus oh wait du har inget.")
                    print()
                    time.sleep(5)
                    print("No money having ass")
                    time.sleep(3)
            elif bchoice == "n":
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

        elif schoice == "2":
            print(Skotterud.name)
            print(Skotterud.category)
            print(str(Skotterud.price) + " kr")
            print("You have the money of: " + str(saldo) + " kr, " + "do you want buy?")
            skchoice = input("j/n: ")
            if skchoice == "j":
                if saldo > Skotterud.price:
                    print("Du bra val, " + Skotterud.name + " köpad")
                    saldo = saldo - Skotterud.price
                    print("Du innehavar nu " + str(saldo) + " peng.")
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
                
        
    elif choice == "2":
        print(str(saldo))

    elif choice == "3":
        looping = False

    else:
        print("Sug mina bollar")