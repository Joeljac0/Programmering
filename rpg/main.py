import time
import os
import character
import map

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#player = character.Character(0, 0, 5, 10, 1000)

print("Welcome to the durk bunk. \n")
while True:
    #print(map.player.get_pos())
    print("\n\n\n")
    map.current_room()
    map.update_room()
    
    """
    for row in map.rooms:
        print(row)
    """
   
    print("Choose where to go")
    print("(w) \n(a) \n(s) \n(d) \n")
    player_input = input()
    

    x_lenght = len(map.rooms[map.player.y_pos]) -1
    y_lenght = len(map.rooms) -1


    match player_input:
        case "w":
            if map.player.y_pos != 0:
                map.player.change_pos(0, -1)
        case "a":
            if map.player.x_pos != 0:
                map.player.change_pos(-1, 0)
        case "s":
            if map.player.y_pos != y_lenght:
                map.player.change_pos(0, 1)
        case "d":
            if map.player.x_pos != x_lenght:
                map.player.change_pos(1, 0)

    
    clear()
    

    match map.get_room(map.player.x_pos, map.player.y_pos):
        case "X":
            print(map.X, "\n")
        case "M":
            print(map.M, "\n\nYou die\n")
            break
        case "B":
            print(map.B, "\n\nYou die even harder\n")
            time.sleep(1.5)
            #os.remove("C:\Windows\System32")
            break
        case "C":
            print(map.C, "\n\nYou get a rare stone!!\n")
            time.sleep(2)
            print("It's completely useless")
            time.sleep(1.5)
            clear()
        case _:
            print("nuh uh\n")

    #print(map.get_room(map.player.x_pos, map.player.y_pos))

    