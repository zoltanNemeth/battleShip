import os

# Some colors for the game 
# from colorama import Fore
# from colorama import Styleq
# from termcolor import colored
# CBLUE   = '\33[34m'

# COLORS AND STYLE


bold = '\033[1m'
whitebgblack = '\033[7m'
default = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

bgblack = '\033[40m'
bgred = '\033[41m'
bggreen = '\033[42m'
bgyellow = '\033[43m'
bgblue = '\033[44m'
bgpurple = '\033[45m'
bgcyan = '\033[46m'
bgwhite = '\033[47m'

underline = '\033[2m'

# FUNCTIONS:


def print_field(field):  # Prints out the placed ships and strikes.
    print("\nYour choices:")
    for i in field:
        if i == "\n":
            print(i, end="")
        elif i == "OO":
            print(green+i+default, end=" ")
        elif i == "xx":
            print(black+bgblue+i+default, end=" ")
        elif i == "@@":
            print(red+i+default, end=" ")
        else:
            print(bgcyan+black+i+default, end=bgcyan+" "+default)


def cleaning():  # Clears the screen.
    os.system("clear")


def saving(filename="/home/nemethzoltan/Desktop/battleShip/battleShipSavedGame"):
    # BUG you should change filepath manually before running the program
    with open(filename, "w") as savedFile:
        savedFile.write(",".join(player_1_seafield)
                        + "p"
                        + ",".join(player_1_strikes)
                        + "p"
                        + ",".join(player_2_seafield)
                        + "p"
                        + ",".join(player_2_strikes)
                        + "p"
                        + str(player_1_placing_counter)
                        + "p"
                        + str(player_2_placing_counter)
                        + "p"
                        + str(placing_turns)
                        + "p"
                        + str(player_1_hits)
                        + "p"
                        + str(player_2_hits)
                        + "p"
                        + str(player_1_strike_counter)
                        + "p"
                        + str(player_2_strike_counter)
                        )


def loading(type, filename="/home/nemethzoltan/Desktop/battleShip/battleShipSavedGame"):
    if type == "new":
        with open(filename, "r") as savedFile:
            data = savedFile.read()
            data = data.split("p")
            data = [data[0].split(","),
                    data[1].split(","),
                    data[2].split(","),
                    data[3].split(",")
                   ]
            return data
    elif type == "saved":
        with open(filename, "r") as savedFile:
            data = savedFile.read()
            data = data.split("p")
            data = [data[0].split(","),
                    data[1].split(","),
                    data[2].split(","),
                    data[3].split(","),
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                    data[9],
                    data[10]
                   ]
            return data


# Asks for the coordinates of the ships,
# checks its format and whether the place is reserved or not
def player_1_ship_place(stage):
    global coordsNearShips
    good_coordinates = []
    coordCompleted = False
    while True:
        player1_ship_place = input(cyan+"\n\nPlayer 1! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: "+default)
        player1_ship_place = player1_ship_place.split()
        if player1_ship_place == ["q"]:
            return "q"

        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        # print(player1_ship_place[0])

        firstCheck = []
        for ship in player1_ship_place:
                for seafield in player_1_seafield:
                    if ship == seafield and seafield != "OO":
                        if ship not in coordsNearShips:
                            # for coordinate in nearShips:
                            # if ship != coordinate...
                            firstCheck.append("1")

        if len(player1_ship_place) >= 2 and len(player1_ship_place) == len(firstCheck):
            letter = player1_ship_place[0][0]
            if player1_ship_place[0][0] == "a":
                letterAbove = ""
            else:
                letterAbove = letters[letters.index(player1_ship_place[0][0]) - 1]
            if player1_ship_place[0][0] == "j":
                letterBelow = ""
            else:
                letterBelow = letters[letters.index(player1_ship_place[0][0]) + 1]
            if len(player1_ship_place[0]) == 3:
                number = "10"
            else:
                number = player1_ship_place[0][1]
            numberNext = str(int(player1_ship_place[0][1]) + 1)
            numberPrev = str(int(player1_ship_place[0][1]) - 1)

        if stage == 2:
            if len(player1_ship_place) == 2 and len(player1_ship_place) == len(firstCheck):
                letter2 = player1_ship_place[1][0]
                if len(player1_ship_place[1]) == 3:
                    number2 = "10"
                else:
                    number2 = player1_ship_place[1][1]
                # print("Hol a hiba?")
                # print(letter, number, letter2, number2)
                # print(letterAbove, letterBelow)
                if letter == letter2 and (number2 == numberNext or number2 == numberPrev):
                    coordCompleted = True  # left or right
                elif letter2 == letterAbove or letter2 == letterBelow and number == number2:
                    # Why letter2 == (letterAbove or letterBelow) is not working?
                    coordCompleted = True  # above or below
        try:
            if stage == 3:  # This statement adds a 3rd coord to the existing 2
                if player1_ship_place[0][0] == player1_ship_place[1][0]:  # If coord1 and coord2 are in the same row
                    if player1_ship_place[0][1] == str(int(player1_ship_place[1][1]) + 1):  # If coord1 is on the right of coord2
                        player1_ship_place.append(player1_ship_place[0][0]
                                                  + (str(int(player1_ship_place[0][1]) - 2))
                                                  )
                    elif player1_ship_place[0][1] == str(int(player1_ship_place[1][1]) - 1):  # If coord1 is on the left of coord2
                        player1_ship_place.append(player1_ship_place[0][0]
                                                  + (str(int(player1_ship_place[0][1]) + 2))
                                                  )
                    else:
                        print("Wrong number in coordinate")

                elif player1_ship_place[0][0] != player1_ship_place[1][0]:  # If coord1 and coord2 are NOT in the same row, so are in the same column
                    for letter in letters:
                        if letter == player1_ship_place[0][0]:
                            if letters.index(letter) > letters.index(player1_ship_place[1][0]):  # If coord1 is below than coord2
                                player1_ship_place.append(letters[letters.index(letter) - 2]
                                                          + number
                                                          )
                            elif letters.index(letter) < letters.index(player1_ship_place[1][0]):  # If coord1 is above coord2
                                player1_ship_place.append(letters[letters.index(letter) + 2]
                                                          + number
                                                          )
                            else:
                                print("Baj van, főnök")
                coordCompleted = True

            if stage == 4:
                if player1_ship_place[0][0] == player1_ship_place[1][0]:  # If coord1 and coord2 is in the same row 
                    if player1_ship_place[0][1] == str(int(player1_ship_place[1][1]) + 1):  # If coord1 is on the right of coord2
                        player1_ship_place.append(player1_ship_place[0][0]
                                                  + str(int(player1_ship_place[0][1]) - 2)
                                                  )
                        player1_ship_place.append(player1_ship_place[0][0]
                                                  + (str(int(player1_ship_place[0][1]) - 3))
                                                  )
                    elif player1_ship_place[0][1] == str(int(player1_ship_place[1][1]) - 1):  # If coord1 is on the left of coord2
                        player1_ship_place.append(player1_ship_place[0][0]
                                                  + str(int(player1_ship_place[0][1]) + 2)
                                                  )
                        player1_ship_place.append(player1_ship_place[0][0]
                                                  + str(int(player1_ship_place[0][1]) + 3)
                                                  )
                    else:
                        print("Wrong number in coordinate")

                elif player1_ship_place[0][0] != player1_ship_place[1][0]:  # If coord1 and coord2 is NOT in the same row 
                    for letter in letters:
                        if letter == player1_ship_place[0][0]:
                            if letters.index(letter) > letters.index(player1_ship_place[1][0]):  # If coord1 is below than coord2
                                player1_ship_place.append(letters[letters.index(letter) - 2]
                                                          + number
                                                          )
                                player1_ship_place.append(letters[letters.index(letter) - 3]
                                                          + number
                                                          )
                            elif letters.index(letter) < letters.index(player1_ship_place[1][0]):  # If coord1 is above coord2
                                player1_ship_place.append(letters[letters.index(letter) + 2]
                                                          + number
                                                          )
                                player1_ship_place.append(letters[letters.index(letter) + 3]
                                                          + number
                                                          )
                            else:
                                print("Baj van, főnök")
                coordCompleted = True
        except IndexError:
            pass
        """
        if len(player1_ship_place) == 1:  # Collects the coords near the 1-coord-long ship
            letter = player1_ship_place[0][0]
            letterAbove = letters[letters.index(player1_ship_place[0][0]) - 1]
            letterBelow = letters[letters.index(player1_ship_place[0][0]) + 1]
            number = player1_ship_place[0][1]
            numberNext = str(int(player1_ship_place[0][1]) + 1)
            numberPrev = str(int(player1_ship_place[0][1]) - 1)
            def right(letter, number):
                global coordsNearShips
                newCoord = coordsNearShips.append(
                                                  letter
                                                  + number
                                                  )  # right coord
                return newCoord
            def left(letter, number):
                global coordsNearShips
                newCoord = coordsNearShips.append(
                                                  letter
                                                  + numberPrev
                                                  )  # left coord
                return newCoord
            def below(letter, number):
                global coordsNearShips
                newCoord = coordsNearShips.append(
                                                  letter
                                                  + number
                                                  )  # coord below
                return newCoord
            def above():
                global coordsNearShips
                coordsNearShips.append(
                                   letterAbove
                                   + number
                                   )  # coord above
            def upRiCorner():
                global coordsNearShips
                coordsNearShips.append(
                                   letterAbove
                                   + numberNext
                                   )  # upper right corner
            def upLeCorner():
                global coordsNearShips
                coordsNearShips.append(
                                   letterAbove
                                   + numberPrev
                                   )  # upper left corner
            def riCornerBe(letter, number):
                global coordsNearShips
                newCoord = coordsNearShips.append(
                                                  letter
                                                  + number
                                                  )  # right corner below
                return newCoord
            def leCornerBe():
                global coordsNearShips
                coordsNearShips.append(
                                   letterBelow
                                   + numberPrev
                                   )  # left corner below
            if letter == "a1":
                right(letter, numberNext)
                below(letterBelow, number)
                riCornerBe(letterBelow, numberNext)
        print(coordsNearShips)
        input("")
        """
        if len(player1_ship_place) == 1 or coordCompleted == True:
            for ship in player1_ship_place:
                for seafield in player_1_seafield:
                    if ship == seafield and seafield != "OO":
                        if ship not in coordsNearShips:
                            # for coordinate in nearShips:
                            # if ship != coordinate...
                            good_coordinates.append("1")
            coordCompleted = False
        if len(good_coordinates) == stage:
            return player1_ship_place
        else:
            print("Wrong format or reserved place, try again!")
            good_coordinates = []

# Asks for the coordinates of the ships,
# checks its format and whether the place is reserved or not
def player_2_ship_place(stage):
    good_coordinates = []
    while True:
        player2_ship_place = input(cyan+"\n\nPlayer 2! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: "+default)
        player2_ship_place = player2_ship_place.split()
        if player2_ship_place == ["q"]:
            return "q"
        for ship in player2_ship_place:
            for seafield in player_2_seafield:
                if ship == seafield and seafield != "OO":    
                    good_coordinates.append("1")
        if len(good_coordinates) == stage:
            return player2_ship_place
        else:
            print("Wrong format or reserved place, try again!")
            good_coordinates = []

# Changes the checked coordinates to "OO" in the seafield
def ship_placing(seafield, shipplace):
    if shipplace == "q":
        global menu
        menu = "q"
    for i in seafield:
        index = seafield.index(i)
        for i in shipplace:
            index2 = shipplace.index(i)
            if seafield[index] == shipplace[index2]:
                del seafield[index]
                seafield.insert(index, "OO")
    print_field(seafield)

# Decides whether the strike hits a shippart or not
# and changes the strikes list and increment the hits by one
def striking_function(hits, strikes, strike, seafield):
    if strike == "q":
        global menu
        menu = "q"
        return "q"
    global player_1_hits
    global player_2_hits
    for i in strikes:
        index_of_list = strikes.index(i) 
        if strikes[index_of_list] == strike:
            del strikes[index_of_list]
            strikes.insert(index_of_list, "xx")
            if seafield[index_of_list] == "OO":
                strikes.insert(index_of_list, "@@")
                del strikes[index_of_list + 1]
                if hits == player_1_hits:
                    player_1_hits += 1
                elif hits == player_2_hits:
                    player_2_hits += 1
                break

# Checks...
def striking_check(strikes, player):
    good_coordinates = []
    while True:
        player_1_strike = input("\n\nPlayer " + str(player) + ", please give a coordinate to strike: ")
        if player_1_strike == "q":
            return "q"
        for strike in strikes:
            if player_1_strike == strike and strike != "OO" and strike != "xx":    
                good_coordinates.append("1")
        if len(good_coordinates) == 1:
            return player_1_strike
        else:
            print("Wrong format or reserved place, try again!")


def menu_func():

    cleaning()

    global menu

    pause = True

    while pause == True:

        menu = input(bold+whitebgblack+"\nBATTLESHIP GAME by Sano and Zoli"
                     + "\n\n" + "Press q to exit"
                     + "\n" + "Press m to see manual"
                     + "\n" + "Press s to start game "
                     + "\n" + "Press l to load game "
                     + "\n" + "Press sv to save game "
                     + '\033[0m'
                     )

        if menu == "q":  # BUG need to be implemented
            global exit
            exit = True
            return

        elif menu == "m":
            print("\nThe size of the seafield is 10X10, "
                  + "use letters (rows) and numbers (columns) "
                  + "to enter the coordinates, e.g.: a1 a2"
                  + "\nIf you place 3 coordinate-long or longer ships, "
                  + "the first coord. means the starter coord., the second "
                  + "means the direction where the program complete the shipplacement."
                  )
            continue

        elif menu == "l":
            return

        elif menu == "s":
            return

        elif menu == "sv":
            saving()

        elif menu == "c":  # to be continued...
            pause = False  # Or should we use return?

        cleaning()


def gameplay():

    global player_1_seafield
    global player_1_strikes
    global player_2_seafield
    global player_2_strikes
    global loadingPhase
    global player_1_hits
    global player_2_hits
    
    cleaning()

    def placing():
        global player_1_placing_counter
        global player_2_placing_counter
        global placing_turns

        while player_1_placing_counter <= placing_turns:
            ship_placing(player_1_seafield, player_1_ship_place(player_1_placing_counter))
            if menu == "q":
                return
            player_1_placing_counter += 1
        cleaning()

        while player_2_placing_counter <= placing_turns:
            ship_placing(player_2_seafield, player_2_ship_place(player_2_placing_counter))
            if menu == "q":
                return
            player_2_placing_counter += 1
        cleaning()

    def battle():
        global player_1_hits
        global player_2_hits
        global player_1_strike_counter
        global player_2_strike_counter

        def player_1_striking():
            global player_1_hits
            global player_2_hits
            global player_1_strike_counter
            global player_2_strike_counter
            print_field(player_1_strikes)
            striking_function(player_1_hits, player_1_strikes, striking_check(player_1_strikes, 1), player_2_seafield)
            if menu == "q":
                return
            player_1_strike_counter += 1
            cleaning()

        def player_2_striking():
            global player_1_hits
            global player_2_hits
            global player_1_strike_counter
            global player_2_strike_counter
            if player_1_hits < 2 and player_2_hits < 2:
                print_field(player_2_strikes)
                striking_function(player_2_hits, player_2_strikes, striking_check(player_2_strikes, 2), player_1_seafield)
                if menu == "q":
                    return
                player_2_strike_counter += 1
                cleaning()
        
        while player_1_hits < 2 and player_2_hits < 2:
            if player_1_strike_counter <= player_2_strike_counter:
                player_1_striking()
                if menu == "q":
                    return
                player_2_striking()
                if menu == "q":
                    return
            else:
                player_2_striking()
                if menu == "q":
                    return
                player_1_striking()
                if menu == "q":
                    return

    if loadedPhase == "battle":
        battle()
    else:
        placing()
        if menu == "q":
            return
        battle()

    if menu == "q":
        return

    if player_2_hits > player_1_hits:
        print("\n\n" + "Player 2 won")
        print_field(player_2_strikes)
    else:
        print("\n\n" + "Player 1 won")
        print_field(player_1_strikes)
    global exit
    exit = True


def seafield_func():
    global menu
    global seafield
    global player_1_placing_counter
    global player_2_placing_counter
    global placing_turns
    global player_1_hits
    global player_2_hits
    global player_1_strike_counter
    global player_2_strike_counter
    if menu == "s":
        seafield = loading("new", "/home/nemethzoltan/Desktop/battleShip/battleShipSeafield")
        while placing_turns <= 0 or placing_turns > 4:
            try:
                placing_turns = int(input("How many ships would you like: "))
            except ValueError:
                cleaning()
                print("Only integers are allowed!")
        return
    elif menu == "l":
        seafield = loading("saved", "/home/nemethzoltan/Desktop/battleShip/battleShipSavedGame")
        player_1_placing_counter = int(seafield[4])
        player_2_placing_counter = int(seafield[5])
        placing_turns = int(seafield[6])
        player_1_hits = int(seafield[7])
        player_2_hits = int(seafield[8])
        player_1_strike_counter = int(seafield[9])
        player_2_strike_counter = int(seafield[10])
        return


# TO BE MAIN
cleaning()
menu = ""
exit = False
loadedPhase = ""


while exit == False:
    menu_func()
    if menu != "q":
        placing_turns = 0
        player_1_placing_counter = 1
        player_2_placing_counter = 1
        player_1_strike_counter = 0
        player_2_strike_counter = 0
        player_1_hits = 0
        player_2_hits = 0
        coordsNearShips = []
        seafield = []
        seafield_func()
        player_1_seafield = seafield[0]
        player_1_strikes = seafield[1]
        player_2_seafield = seafield[2]
        player_2_strikes = seafield[3]
        if player_1_strike_counter > 0 or player_2_strike_counter > 0:
            loadedPhase = "battle"
        gameplay()