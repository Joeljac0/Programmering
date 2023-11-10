import tkinter


window = tkinter.Tk()
window.title("Glosor")
label = tkinter.Label(window,text = "Skriv Svensk glosa och dess motsvarande engelska glosa").pack()
input_glos= tkinter.Entry(window).place(y=50)
input_glos2= tkinter.Entry(window).place(y=75)

print('Glos? \n')

gloslist=[]

mata='j'
i=0

while (mata != 'n'):
    glos=[]
    #input_glos = input("Skriv en svensk glosa: ")
    #nput_glos2 = input("Skriv en engelsk glosa: ")
    glos.append(str(input_glos))
    glos.append(str(input_glos2))

    gloslist.append(glos)
    mata = input('Vill du mata in mer glosor? \n j/n: ')
    i = i+1

mata='j'

while (mata != 'n'):
    print ('\n nu startar provet\n')
    antalR = 0
    antalG = len(gloslist)

    for a in gloslist:
        sv_glos=a[0] + ' = '
        en_glos=a[1]

        tglos = input(sv_glos)

        if tglos == en_glos:
            print('Korrekt! \n')
            antalR=antalR+1
        
        else:
            print('fel! Korrekt svar: ', en_glos, '\n')

        
    if antalR==antalG:
        print('Alla rätt! \n')
    else:
        print('Du hade', antalR, ' av ', antalG, 'glosor \n')

    mata = input('Vill du repetera provet j/n? \n')

    