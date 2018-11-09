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
                        + "p"
                        + ",".join(coordsNearShips1)
                        + "p"
                        + ",".join(coordsNearShips2)
                        )


def loading(type, filename="/home/nemethzoltan/Desktop/battleShip/battleShipSavedGame"):
    if type == "new":
        with open(filename, "r") as savedFile:
            data = savedFile.read()
            data = data.split("p")
            data = [
                   data[0].split(","),
                   data[1].split(","),
                   data[2].split(","),
                   data[3].split(",")
            ]
            return data
    elif type == "saved":
        with open(filename, "r") as savedFile:
            data = savedFile.read()
            data = data.split("p")
            data = [
                   data[0].split(","),
                   data[1].split(","),
                   data[2].split(","),
                   data[3].split(","),
                   data[4],
                   data[5],
                   data[6],
                   data[7],
                   data[8],
                   data[9],
                   data[10],
                   data[11].split(","),
                   data[12].split(",")
            ]
            return data


def new_placing(coordinates, stage, player_1_seafield):

    from commonFunctions import letter, letterAbove, letterBelow
    from commonFunctions import number, numberNext, numberPrev
    from commonFunctions import position, coord1IsOnWhatSideOfCoord2

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    # print(coordinates[0])

    firstCheck = []
    for ship in coordinates:
            for seafield in player_1_seafield:
                if ship == seafield and seafield != "OO":
                    # if ship not in coordsNearShips:
                        # for coordinate in nearShips:
                        # if ship != coordinate...
                    firstCheck.append("1")

    if len(coordinates) >= 2 and len(coordinates) == len(firstCheck):

        if stage == 2:
            if len(coordinates) == 2 and len(coordinates) == len(firstCheck):
                letter1 = letter(coordinates)
                letter2 = letter(coordinates, 1)
                number1 = number(coordinates)
                number2 = number(coordinates, 1)
                firstCoord = coordinates[0]
                # print("Hol a hiba?")
                # print(letter1, number1, letter2, number2)
                # print(letterAbove, letterBelow)
                if letter1 == letter2 and (number2 == numberNext(firstCoord) or number2 == numberPrev(firstCoord)):
                    return coordinates  # left or right
                elif letter2 == letterAbove(firstCoord) or letter2 == letterBelow(firstCoord) and number1 == number2:
                    # Why letter2 == (letterAbove or letterBelow) is not working?
                    return coordinates  # above or below
                else:
                    coordinates = False
                    return coordinates
        try:
            if stage == 3:  # This statement adds a 3rd coord to the existing 2
                if position(coordinates) == "horizontal":  # If coord1 and coord2 are in the same row
                    if coord1IsOnWhatSideOfCoord2(coordinates) == "right":  # If coord1 is on the right of coord2
                        coordinates.append(letter(coordinates)
                                                  + (str(int(coordinates[0][1]) - 2))
                                                  )
                    elif coord1IsOnWhatSideOfCoord2(coordinates) == "left":  # If coord1 is on the left of coord2
                        coordinates.append(coordinates[0][0]
                                                  + (str(int(coordinates[0][1]) + 2))
                                                  )
                    else:
                        coordinates = False
                        return coordinates

                elif position(coordinates) == "vertical":  # If coord1 and coord2 are NOT in the same row, so are in the same column
                    for letter in letters:
                        if letter == coordinates[0][0]:
                            if letters.index(letter) > letters.index(coordinates[1][0]):  # If coord1 is below than coord2
                                if (letters.index(letter) - 2) > 0:
                                    # print("Here I am", coordinates)  # Only for debugging
                                    # print(letterAbove(coordinates[-1]))  # Only for debugging
                                    # print(number(coordinates))  # Only for debugging
                                    coordinates.append(
                                        letterAbove(coordinates[-1])
                                        + number(coordinates)
                                    )
                                    # print("Here I am2", coordinates)  # Only for debugging
                                else:
                                    coordinates = False
                                    return coordinates
                            elif letters.index(letter) < letters.index(coordinates[1][0]):  # If coord1 is above coord2
                                coordinates.append(letters[letters.index(letter) + 2]
                                                          + number(coordinates)
                                                          )
                            else:
                                coordinates = False
                                return coordinates
                return coordinates

            if stage == 4:
                if coordinates[0][0] == coordinates[1][0]:  # If coord1 and coord2 is in the same row 
                    if coordinates[0][1] == str(int(coordinates[1][1]) + 1):  # If coord1 is on the right of coord2
                        coordinates.append(coordinates[0][0]
                                                  + str(int(coordinates[0][1]) - 2)
                                                  )
                        coordinates.append(coordinates[0][0]
                                                  + (str(int(coordinates[0][1]) - 3))
                                                  )
                    elif coordinates[0][1] == str(int(coordinates[1][1]) - 1):  # If coord1 is on the left of coord2
                        coordinates.append(coordinates[0][0]
                                                  + str(int(coordinates[0][1]) + 2)
                                                  )
                        coordinates.append(coordinates[0][0]
                                                  + str(int(coordinates[0][1]) + 3)
                                                  )
                    else:
                        coordinates = False
                        return coordinates

                elif coordinates[0][0] != coordinates[1][0]:  # If coord1 and coord2 is NOT in the same row 
                    for letter in letters:
                        if letter == coordinates[0][0]:
                            if letters.index(letter) > letters.index(coordinates[1][0]):  # If coord1 is below than coord2
                                # print("Here I am")  # Only for debugging
                                if (letters.index(letter) - 3) >= 0:
                                    # print("Here I am")  # Only for debugging
                                    coordinates.append(letters[letters.index(letter) - 2]
                                                              + number(coordinates)
                                                              )
                                    coordinates.append(letters[letters.index(letter) - 3]
                                                              + number(coordinates)
                                                              )
                                else:
                                    coordinates = False
                                    return coordinates
                            elif letters.index(letter) < letters.index(coordinates[1][0]):  # If coord1 is above coord2
                                coordinates.append(letters[letters.index(letter) + 2]
                                                          + number(coordinates)
                                                          )
                                coordinates.append(letters[letters.index(letter) + 3]
                                                          + number(coordinates)
                                                          )
                            else:
                                coordinates = False
                                return coordinates
                return coordinates
        except IndexError:
            coordinates = False
            return coordinates

def collectCoordsNearShip(stage, coordsOfShip, coordsNearShips):

    from commonFunctions import letter, letterAbove, letterBelow
    from commonFunctions import number, numberNext, numberPrev
    from commonFunctions import position, rowsBeside, columnsBeside, isReverse

    # global coordsNearShips1  # Only for debugging
    # global coordsNearShips2  # Only for debugging
    
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

    if stage == 1:  # Collects the coords near the 1-coord-long ship
            
        coordsNearShips.extend(
            [
            letter(coordsOfShip) + numberNext(coordsOfShip[0]),  # right coord
            letter(coordsOfShip) + numberPrev(coordsOfShip[0]),  # left coord
            letterBelow(coordsOfShip[0]) + number(coordsOfShip),  # coord below
            letterAbove(coordsOfShip[0]) + number(coordsOfShip),  # coord above
            letterAbove(coordsOfShip[0]) + numberNext(coordsOfShip[0]),  # upper right corner
            letterAbove(coordsOfShip[0]) + numberPrev(coordsOfShip[0]),  # upper left corner
            letterBelow(coordsOfShip[0]) + numberNext(coordsOfShip[0]),  # right corner below
            letterBelow(coordsOfShip[0]) + numberPrev(coordsOfShip[0])  # left corner below
            ]
        )

    if stage >= 2:
        if position(coordsOfShip) == "horizontal":
            # print("horizontal")  # Only for debugging
            rowsBeside(coordsOfShip, coordsNearShips)
            columnsBeside(coordsOfShip, coordsNearShips)
        else:  # If vertical
            # print("vertical")  # Only for debugging
            if isReverse(coordsOfShip) == True:
                # print("reverse")  # Only for debugging
                endAbove = letterBelow(coordsOfShip[0]) + number(coordsOfShip)
                endBelow = letterAbove(coordsOfShip[-1]) + number(coordsOfShip, -1)
            else:  # If not reversed
                endAbove = letterAbove(coordsOfShip[0]) + number(coordsOfShip)
                endBelow = letterBelow(coordsOfShip[-1]) + number(coordsOfShip, -1)

            if endAbove != "a":
                coordsNearShips.extend(  # Add to coordsNearShips the row above of the ship
                    [
                    letter(endAbove) + numberPrev(endAbove),
                    endAbove,
                    letter(endAbove) + numberNext(endAbove)
                    ]
                )
            if endBelow != "j":
                coordsNearShips.extend(  # Add to coordsNearShips the row below of the ship
                    [
                    letter(endBelow) + numberPrev(endBelow),
                    endBelow,
                    letter(endBelow) + numberNext(endBelow)
                    ]
                )

            for coordinate in coordsOfShip:
                coordsNearShips.extend(
                    [
                    letter(coordinate) + numberPrev(coordinate),
                    letter(coordinate) + numberNext(coordinate)
                    ]
                )

# Asks for the coordinates of the ships,
# checks its format and whether the place is reserved or not
def player_1_ship_place(stage):
    from commonFunctions import isInputValid
    global coordsNearShips1
    good_coordinates = []
    while True:
        player1_ship_place = input(cyan+"\n\nPlayer 1! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: "+default)
        player1_ship_place = player1_ship_place.split()
        if player1_ship_place == ["q"]:
            return "q"
        if len(player1_ship_place) != 1:
            # if isInputValid(stage, player1_ship_place, player_1_seafield) == True:
            player1_ship_place = new_placing(player1_ship_place, stage, player_1_seafield)
        # print(player1_ship_place)  # Only for debugging
        if type(player1_ship_place) != bool:
            try:
                if len(player1_ship_place) >= 1:
                    if isInputValid(stage, player1_ship_place, player_1_seafield) == True:
                        # print("len of... ", len(player1_ship_place))  # Only for debugging
                        collectCoordsNearShip(stage, player1_ship_place, coordsNearShips1)
                        # print(coordsNearShips1)  # Only for debugging
                        # print(coordsNearShips2)  # Only for debugging
                        for ship in player1_ship_place:
                            for seafield in player_1_seafield:
                                if ship == seafield and seafield != "OO" and ship not in coordsNearShips1:
                                    good_coordinates.append("1")
                                    # print(good_coordinates)  # Only for debugging
            except TypeError:
                pass
        if len(good_coordinates) == stage:
            return player1_ship_place
        else:
            print("Wrong format or reserved place, try again!")
            good_coordinates = []
            if type(player1_ship_place) != bool:
                if isInputValid(stage, player1_ship_place, player_1_seafield) == True:
                    wrongCoords = []
                    collectCoordsNearShip(stage, player1_ship_place, wrongCoords)
                    for coordinate in wrongCoords:
                        coordsNearShips1.remove(coordinate)

# Asks for the coordinates of the ships,
# checks its format and whether the place is reserved or not
def player_2_ship_place(stage):
    from commonFunctions import isInputValid
    good_coordinates = []
    global coordsNearShips2
    while True:
        player2_ship_place = input(cyan+"\n\nPlayer 2! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: "+default)
        player2_ship_place = player2_ship_place.split()
        if player2_ship_place == ["q"]:
            return "q"

        if len(player2_ship_place) != 1:
            # if isInputValid(stage, player2_ship_place, player_2_seafield) == True:
            player2_ship_place = new_placing(player2_ship_place, stage, player_2_seafield)

        if type(player2_ship_place) != bool:
            # print("not bool", player2_ship_place)  # Only for debugging
            try:
                if len(player2_ship_place) >= 1:
                    # print("bigger than 0")  # Only for debugging
                    if isInputValid(stage, player2_ship_place, player_2_seafield) == True:
                        collectCoordsNearShip(stage, player2_ship_place, coordsNearShips2)
                        # print(coordsNearShips1)  # Only for debugging
                        # print(coordsNearShips2)  # Only for debugging
                        for ship in player2_ship_place:
                            for seafield in player_2_seafield:
                                if ship == seafield and seafield != "OO" and ship not in coordsNearShips2:
                                    good_coordinates.append("1")
            except TypeError:
                pass
        if len(good_coordinates) == stage:
            return player2_ship_place
        else:
            print("Wrong format or reserved place, try again!")
            good_coordinates = []
            if type(player2_ship_place) != bool:
                if isInputValid(stage, player2_ship_place, player_2_seafield) == True:
                    wrongCoords = []
                    collectCoordsNearShip(stage, player2_ship_place, wrongCoords)
                    for coordinate in wrongCoords:
                        coordsNearShips2.remove(coordinate)

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
def striking_function(player, strikes, strike, seafield):
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
                if player == "player 1":
                    player_1_hits += 1
                elif player == "player 2":
                    player_2_hits += 1
                break

# Checks...
def striking_check(strikes, player):
    good_coordinates = []
    while True:
        new_strike = input("\n\nPlayer " + str(player) + ", please give a coordinate to strike: ")
        if new_strike == "q":
            return "q"
        for strike in strikes:
            if new_strike == strike and strike != "OO" and strike != "xx":    
                good_coordinates.append("1")
        if len(good_coordinates) == 1:
            return new_strike
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
    if menu == "q":
        return

    def placing():
        global player_1_placing_counter
        global player_2_placing_counter
        global placing_turns

        while player_1_placing_counter <= placing_turns:
            ship_placing(player_1_seafield, player_1_ship_place(player_1_placing_counter))
            if menu == "q":
                # print(coordsNearShips1)  # Only for debugging
                # print(coordsNearShips2)  # Only for debugging
                a = input("Press enter to continue ")
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
            # print(player_1_hits, player_1_strike_counter)  # Only for debugging
            # print(player_2_hits, player_2_strike_counter)  # Only for debugging
            striking_function("player 1", player_1_strikes, striking_check(player_1_strikes, 1), player_2_seafield)
            if menu == "q":
                return
            player_1_strike_counter += 1
            cleaning()

        def player_2_striking():
            global player_1_hits
            global player_2_hits
            global player_1_strike_counter
            global player_2_strike_counter
            print_field(player_2_strikes)
            # print(player_1_hits, player_1_strike_counter)  # Only for debugging
            # print(player_2_hits, player_2_strike_counter)  # Only for debugging
            striking_function("player 2", player_2_strikes, striking_check(player_2_strikes, 2), player_1_seafield)
            if menu == "q":
                return
            player_2_strike_counter += 1
            cleaning()
        
        while player_1_hits < maxHits and player_2_hits < maxHits:
            if player_1_strike_counter <= player_2_strike_counter:
                player_1_striking()
                if menu == "q":
                    return
            else:
                player_2_striking()
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
        # print(player_1_hits, player_1_strike_counter)  # Only for debugging
        # print(player_2_hits, player_2_strike_counter)  # Only for debugging
        print("\n\n" + "Player 2 won in", player_2_strike_counter, "turns.")
        print("Player 1 would need", maxHits - player_1_hits, "more hit(s).")
        print_field(player_2_strikes)
    elif player_2_hits < player_1_hits:
        # print(player_1_hits, player_1_strike_counter)  # Only for debugging
        # print(player_2_hits, player_2_strike_counter)  # Only for debugging
        print("\n\n" + "Player 1 won in", player_1_strike_counter, "turns.")
        print("Player 2 would need", maxHits - player_2_hits, "more hit(s).")
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
            x = False
            while x is False:
                placing_turns = "a"
                while type(placing_turns) != int:
                    try:
                        placing_turns = input("How many ships would you like? ")
                        if placing_turns != "q":
                            placing_turns = int(placing_turns)
                    except ValueError:
                        print("Only integers are allowed!")
                    if placing_turns == "q":
                        menu = "q"
                        return
                    x = True
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
        coordsNearShips1 = seafield[11]
        coordsNearShips2 = seafield[12]
        # print(coordsNearShips1)  # Only for debugging
        # print(coordsNearShips2)  # Only for debugging
        # a = input("press enter to continue")  # Only for debugging
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
        maxHits = 0
        coordsNearShips1 = []
        coordsNearShips2 = []
        seafield = []
        seafield_func()
        player_1_seafield = seafield[0]
        player_1_strikes = seafield[1]
        player_2_seafield = seafield[2]
        player_2_strikes = seafield[3]
        if player_1_strike_counter > 0 or player_2_strike_counter > 0:
            loadedPhase = "battle"

        if placing_turns == 1:
            maxHits = 1
        elif placing_turns == 2:
            maxHits = 3
        elif placing_turns == 3:
            maxHits = 6
        else:
            maxHits = 10

        gameplay()
        # print(coordsNearShips1)  # Only for debugging
        # print(coordsNearShips2)  # Only for debugging
        # a = input("Press enter to continue ")  # Only for debugging
        # saving()  # Only for debugging