import lastbil
import personbil

looping = True

toyota_pink = personbil.Personbil("Toyota", "pink", 40)
ford_red = personbil.Personbil("Ford", "Red", 65)

man_black = lastbil.lastbil("Man", "Black", 450)
ford_pink = lastbil.lastbil("Ford", "Pink", 320)

truck_list = [man_black, ford_pink]
car_list = [toyota_pink, ford_red]

def print_vehicle_list(vehicle_list):
    for vehicle in vehicle_list:
        vehicle.print_fordon()

while looping:
    print("Olika fordon till salu")
    print("(1) Alla fordon")
    print("(2) Alla bilar")
    print("(3) Alla lastbilar")
    print("(4) Avsluta")
    choice = input("Val: ")
    if choice == "1":
      print("Alla fordon:")
      print_vehicle_list(truck_list)
      print_vehicle_list(car_list)
    elif choice == "2":
        print("Alla lastbilar:")
        print_vehicle_list(truck_list)
    elif choice == "3":
        print("Alla bilar:")
        print_vehicle_list(car_list)
    elif choice == "4":
        looping = False

    else:
        print("invalid choice")