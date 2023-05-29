import os
import jokehandler



def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n-Förläng livet med skratt och roliga historier")

    url = f"https://v2.jokeapi.dev/joke/Dark,Spooky?type=single"

    nr = 1
    jokeobject = jokehandler.Jokehandler(url)

    while True:

        t_joke = jokeobject.get_joke()

        print(f"\n{nr}.---------------------------------------------------")
        print(f"{t_joke}")
        print("-----------------------------------------------------")

        nr += 1

        entill = input("Vill du höra ett skämt till? j/n ")

        if(entill == "n" or entill =="N"):
            break

main()