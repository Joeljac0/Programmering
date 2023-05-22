from tkinter import *
from tkinter import messagebox
import lottery

# create root window
root = Tk()
root.title("lottery")

# create listbox
listbox = Listbox(root,
                  height=4,
                  width=30,
                  bg="white",
                  activestyle="dotbox",
                  font="helvetica",
                  fg = "black")

# Definerar storlek på fönster
root.geometry("380x300")

lotteriet = lottery.lottery()

# skapar label
label_antal = Label(root, text="antal lotter, max 3st: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

# skapar textfält
textbox_antal = Entry(root,width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def update_listbox(antal_lott):
    # tömmer listboxen
    listbox.delete(0, END)
    # lägger till text elementen
    listbox.insert(1, "Grattis du vann!")

    try:
        int_antal_lotter = int(antal_lott)
        i=0

        if (int_antal_lotter < 4):
            
            while i <int_antal_lotter:
                vinst = lotteriet.get_vinst()
                listbox.insert((i+2), vinst)
                i +=1
        
        else: 
            (messagebox.showinfo("Too many"))

    except ValueError:
        messagebox.showinfo("ERROR")


def clickSlumpButton():
    #print("tryck")
    antal_lott = textbox_antal.get()
    print(f"tryck {antal_lott}")

    #tömmer listbox
    textbox_antal.delete(0, END)
    #sätter focus på första entry
    textbox_antal.focus_set()
    update_listbox(antal_lott)


# skapar knapp
button_slimpa = Button(text="TUR KNAPP!", command=clickSlumpButton)
button_slimpa.grid(row=1, column=0, sticky=E, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)



root.mainloop()