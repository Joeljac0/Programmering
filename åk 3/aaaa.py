import ikea

looping = True

Billy = ikea.ikea("Billy", "bokhylla", 599)
Skotterud = ikea.ikea("Skotterud", "resårbotten", 4295)


list = [Billy, Skotterud]

#for ikea in list:
#    print(ikea.price)

while looping:
    print("(1) Lista av Möbler")
    print("(2) Avsluta")
    choice = input("Val: ")
    if choice == "1":
        print("Möbler")

        i=0

        for ikea in list:
            print("(" + str(i+1) + ") " + ikea.name)
        
    elif choice == "2":
        looping = False

    else:
        print("invalid choice")