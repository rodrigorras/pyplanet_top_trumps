# Planets Top Trumps - www.101computing.net/planets-top-trumps/
import random
import time

round_counter = 0
player_score = 0
computer_score = 0

print(" ______________________________ ")
print("|                              |")
print("|      Planets Top Trumps      |")
print("|______________________________|")
print("")
# Planet;Distance from Sun (in million km);Size (Diameter in km);Orbital Period (in days);Number of Moons;

labels = ["Planet", "Distance from the Sun", "Diameter", "Orbital Period", "Number of Moons"]

planets = []
planets.append(["Mercury", 57.9, 4879, 88, 0])
planets.append(["Venus", 108.2, 12104, 224.7, 0])
planets.append(["Earth", 149.6, 12756, 365.2, 1])
planets.append(["Mars", 227.9, 6792, 687, 2])
planets.append(["Jupiter", 778.6, 142984, 4331, 67])
planets.append(["Saturn", 1433.5, 120536, 10747, 62])
planets.append(["Uranus", 2872.5, 51118, 30589, 27])
planets.append(["Neptune", 4495.1, 49528, 59800, 14])
planets.append(["Pluto", 5906.4, 2370, 90560, 5])

while (computer_score < 12 or player_score < 12 or len(planets) <= 2):
    print("ROUND ", round_counter)
    print("Your Card:")
    Player_cardNumber = random.randint(0, len(planets) - 1)
    print("---> Planet: " + planets[Player_cardNumber][0])
    print("---> Distance from the Sun: " + str(planets[Player_cardNumber][1]) + " million km.")
    print("---> Diameter: " + str(planets[Player_cardNumber][2]) + " km.")
    print("---> Orbital Period: " + str(planets[Player_cardNumber][3]) + " days.")
    print("---> Number of Moons: " + str(planets[Player_cardNumber][4]))

    # print("Length of planets after pick..." , len(planets), "\n")

    # Complete the code from here...
    print("Computer is picking the card...")
    Computer_cardNumber = random.randint(0, len(planets) - 1)
    # print("---> Planet: " + planets[Computer_cardNumber][0])
    # print("---> Distance from the Sun: " + str(planets[Computer_cardNumber][1])+ " million km.")
    # print("---> Diameter: " + str(planets[Computer_cardNumber][2])+ " km.")
    # print("---> Orbital Period: " + str(planets[Computer_cardNumber][3])+ " days.")
    # print("---> Number of Moons: " + str(planets[Computer_cardNumber][4]))

    print(" ____________________________________ ")
    print("| Pick a Parameter(Pick a number!):  |")
    print("|     1- Distance from the Sun       |")
    print("|     2- Diameter                    |")
    print("|     3- Orbital Period              |")
    print("|     4- Number of Moons             |")
    print("|___________________________________ |")

    compare_parameter = input("Pick a Parameter to Compare: ")
    print("Choosen Parameter = ", labels[int(compare_parameter)])

    print("Calculating who won this round...")
    for i in range(2, 0, -1):
        time.sleep(1)

    if planets[int(Player_cardNumber)][int(compare_parameter)] > planets[int(Computer_cardNumber)][
        int(compare_parameter)]:
        print("Player Won this round!...")

        for i in range(2, 0, -1):
            time.sleep(1)

        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")
        player_score = player_score + 3

        for i in range(2, 0, -1):
            time.sleep(1)
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")


    elif planets[int(Player_cardNumber)][int(compare_parameter)] == planets[int(Computer_cardNumber)][
        int(compare_parameter)]:
        for i in range(2, 0, -1):
            time.sleep(1)
        player_score = player_score + 1
        computer_score = computer_score + 1
        print("it's Draw")
        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")

        for i in range(2, 0, -1):
            time.sleep(1)
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")
    else:
        for i in range(2, 0, -1):
            time.sleep(1)
        print("Loss")
        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("|         Diameter ->", planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("|         Diameter ->", planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")
        computer_score = computer_score + 3
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")

    round_counter = round_counter + 1

    for i in range(2, 0, -1):
        time.sleep(1)
    print("Removing cards from set...")
    if len(planets) <=2:
        print("no more cards, game is over.......")
        break

    print("\n \n")# Planets Top Trumps - www.101computing.net/planets-top-trumps/
import random
import time

round_counter = 0
player_score = 0
computer_score = 0
# Planets Top Trumps - www.101computing.net/planets-top-trumps/
import random
import time

round_counter = 0
player_score = 0
computer_score = 0

print(" ______________________________ ")
print("|                              |")
print("|      Planets Top Trumps      |")
print("|______________________________|")
print("")
# Planet;Distance from Sun (in million km);Size (Diameter in km);Orbital Period (in days);Number of Moons;

labels = ["Planet", "Distance from the Sun", "Diameter", "Orbital Period", "Number of Moons"]

planets = []
planets.append(["Mercury", 57.9, 4879, 88, 0])
planets.append(["Venus", 108.2, 12104, 224.7, 0])
planets.append(["Earth", 149.6, 12756, 365.2, 1])
planets.append(["Mars", 227.9, 6792, 687, 2])
planets.append(["Jupiter", 778.6, 142984, 4331, 67])
planets.append(["Saturn", 1433.5, 120536, 10747, 62])
planets.append(["Uranus", 2872.5, 51118, 30589, 27])
planets.append(["Neptune", 4495.1, 49528, 59800, 14])
planets.append(["Pluto", 5906.4, 2370, 90560, 5])

while (computer_score < 12 or player_score < 12 or len(planets) <= 2):
    print("ROUND ", round_counter)
    print("Your Card:")
    Player_cardNumber = random.randint(0, len(planets) - 1)
    print("---> Planet: " + planets[Player_cardNumber][0])
    print("---> Distance from the Sun: " + str(planets[Player_cardNumber][1]) + " million km.")
    print("---> Diameter: " + str(planets[Player_cardNumber][2]) + " km.")
    print("---> Orbital Period: " + str(planets[Player_cardNumber][3]) + " days.")
    print("---> Number of Moons: " + str(planets[Player_cardNumber][4]))

    # print("Length of planets after pick..." , len(planets), "\n")

    # Complete the code from here...
    print("Computer is picking the card...")
    Computer_cardNumber = random.randint(0, len(planets) - 1)
    # print("---> Planet: " + planets[Computer_cardNumber][0])
    # print("---> Distance from the Sun: " + str(planets[Computer_cardNumber][1])+ " million km.")
    # print("---> Diameter: " + str(planets[Computer_cardNumber][2])+ " km.")
    # print("---> Orbital Period: " + str(planets[Computer_cardNumber][3])+ " days.")
    # print("---> Number of Moons: " + str(planets[Computer_cardNumber][4]))

    print(" ____________________________________ ")
    print("| Pick a Parameter(Pick a number!):  |")
    print("|     1- Distance from the Sun       |")
    print("|     2- Diameter                    |")
    print("|     3- Orbital Period              |")
    print("|     4- Number of Moons             |")
    print("|___________________________________ |")

    compare_parameter = input("Pick a Parameter to Compare: ")
    print("Choosen Parameter = ", labels[int(compare_parameter)])

    print("Calculating who won this round...")
    for i in range(2, 0, -1):
        time.sleep(1)

    if planets[int(Player_cardNumber)][int(compare_parameter)] > planets[int(Computer_cardNumber)][
        int(compare_parameter)]:
        print("Player Won this round!...")

        for i in range(2, 0, -1):
            time.sleep(1)

        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")
        player_score = player_score + 3

        for i in range(2, 0, -1):
            time.sleep(1)
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")


    elif planets[int(Player_cardNumber)][int(compare_parameter)] == planets[int(Computer_cardNumber)][
        int(compare_parameter)]:
        for i in range(2, 0, -1):
            time.sleep(1)
        player_score = player_score + 1
        computer_score = computer_score + 1
        print("it's Draw")
        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")

        for i in range(2, 0, -1):
            time.sleep(1)
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")
    else:
        for i in range(2, 0, -1):
            time.sleep(1)
        print("Loss")
        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("|         Diameter ->", planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("|         Diameter ->", planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")
        computer_score = computer_score + 3
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")

    round_counter = round_counter + 1

    for i in range(2, 0, -1):
        time.sleep(1)
    print("Removing cards from set...")
    if len(planets) <=2:
        print("no more cards, game is over.......")
        break

    print("\n \n")
    if Player_cardNumber == Computer_cardNumber:
        planets.remove(planets[Player_cardNumber])
    else:
        planets.remove(planets[Player_cardNumber])
        planets.remove(planets[Computer_cardNumber])
    print(planets)

if player_score >= 12:
    print("Congratulations ! you Won")
else:
    print("You loss!")
# print("Next Round")
print(" ______________________________ ")
print("|                              |")
print("|      Planets Top Trumps      |")
print("|______________________________|")
print("")
# Planet;Distance from Sun (in million km);Size (Diameter in km);Orbital Period (in days);Number of Moons;

labels = ["Planet", "Distance from the Sun", "Diameter", "Orbital Period", "Number of Moons"]

planets = []
planets.append(["Mercury", 57.9, 4879, 88, 0])
planets.append(["Venus", 108.2, 12104, 224.7, 0])
planets.append(["Earth", 149.6, 12756, 365.2, 1])
planets.append(["Mars", 227.9, 6792, 687, 2])
planets.append(["Jupiter", 778.6, 142984, 4331, 67])
planets.append(["Saturn", 1433.5, 120536, 10747, 62])
planets.append(["Uranus", 2872.5, 51118, 30589, 27])
planets.append(["Neptune", 4495.1, 49528, 59800, 14])
planets.append(["Pluto", 5906.4, 2370, 90560, 5])

while (computer_score < 12 or player_score < 12 or len(planets) <= 2):
    print("ROUND ", round_counter)
    print("Your Card:")
    Player_cardNumber = random.randint(0, len(planets) - 1)
    print("---> Planet: " + planets[Player_cardNumber][0])
    print("---> Distance from the Sun: " + str(planets[Player_cardNumber][1]) + " million km.")
    print("---> Diameter: " + str(planets[Player_cardNumber][2]) + " km.")
    print("---> Orbital Period: " + str(planets[Player_cardNumber][3]) + " days.")
    print("---> Number of Moons: " + str(planets[Player_cardNumber][4]))

    # print("Length of planets after pick..." , len(planets), "\n")

    # Complete the code from here...
    print("Computer is picking the card...")
    Computer_cardNumber = random.randint(0, len(planets) - 1)
    # print("---> Planet: " + planets[Computer_cardNumber][0])
    # print("---> Distance from the Sun: " + str(planets[Computer_cardNumber][1])+ " million km.")
    # print("---> Diameter: " + str(planets[Computer_cardNumber][2])+ " km.")
    # print("---> Orbital Period: " + str(planets[Computer_cardNumber][3])+ " days.")
    # print("---> Number of Moons: " + str(planets[Computer_cardNumber][4]))

    print(" ____________________________________ ")
    print("| Pick a Parameter(Pick a number!):  |")
    print("|     1- Distance from the Sun       |")
    print("|     2- Diameter                    |")
    print("|     3- Orbital Period              |")
    print("|     4- Number of Moons             |")
    print("|___________________________________ |")

    compare_parameter = input("Pick a Parameter to Compare: ")
    print("Choosen Parameter = ", labels[int(compare_parameter)])

    print("Calculating who won this round...")
    for i in range(2, 0, -1):
        time.sleep(1)

    if planets[int(Player_cardNumber)][int(compare_parameter)] > planets[int(Computer_cardNumber)][
        int(compare_parameter)]:
        print("Player Won this round!...")

        for i in range(2, 0, -1):
            time.sleep(1)

        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")
        player_score = player_score + 3

        for i in range(2, 0, -1):
            time.sleep(1)
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")


    elif planets[int(Player_cardNumber)][int(compare_parameter)] == planets[int(Computer_cardNumber)][
        int(compare_parameter)]:
        for i in range(2, 0, -1):
            time.sleep(1)
        player_score = player_score + 1
        computer_score = computer_score + 1
        print("it's Draw")
        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("| Parameter: ", labels[int(compare_parameter)], " ->",
              planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")

        for i in range(2, 0, -1):
            time.sleep(1)
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")
    else:
        for i in range(2, 0, -1):
            time.sleep(1)
        print("Loss")
        print(" ______________________________ ")
        print("| Player  Planet -> ", planets[Player_cardNumber][0])
        print("|         Diameter ->", planets[int(Player_cardNumber)][int(compare_parameter)])
        print("| Computer  Planet -> ", planets[Computer_cardNumber][0])
        print("|         Diameter ->", planets[int(Computer_cardNumber)][int(compare_parameter)])
        print("|______________________________|")
        computer_score = computer_score + 3
        print("------------------")
        print("Your Score", player_score)
        print("Computer Score", computer_score)
        print("-------------------")

    round_counter = round_counter + 1

    for i in range(2, 0, -1):
        time.sleep(1)
    print("Removing cards from set...")
    if len(planets) <=2:
        print("no more cards, game is over.......")
        break

    print("\n \n")
    if Player_cardNumber == Computer_cardNumber:
        planets.remove(planets[Player_cardNumber])
    else:
        planets.remove(planets[Player_cardNumber])
        planets.remove(planets[Computer_cardNumber])
    print(planets)

if player_score >= 12:
    print("Congratulations ! you Won")
else:
    print("You loss!")
# print("Next Round")
    if Player_cardNumber == Computer_cardNumber:
        planets.remove(planets[Player_cardNumber])
    else:
        planets.remove(planets[Player_cardNumber])
        planets.remove(planets[Computer_cardNumber])
    print(planets)

if player_score >= 12:
    print("Congratulations ! you Won")
else:
    print("You loss!")
# print("Next Round")