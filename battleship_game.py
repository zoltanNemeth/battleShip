import os

fileDir = os.path.dirname(os.path.abspath(__file__))

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


def saving(filename=fileDir + "/battleShipSavedGame"):
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
                        + ",".join(coordsNearShip1)
                        + "p"
                        + ",".join(coordsNearShip2)
                        )


def loading(type, filename=fileDir + "/battleShipSavedGame"):
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


def new_placing(coordinates, stage, seafield):

    from commonFunctions import letter, letterAbove, letterBelow
    from commonFunctions import number, numberNext, numberPrev
    from commonFunctions import position, isInputValid, letters, coord1IsOnWhatSideOfCoord2

    # print(coordinates, stage)  # Only for debugging

    if len(coordinates) >= 2 and isInputValid(coordinates, seafield) is True:

        if stage == 2:
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
        # try:
        # print(".")  # Only for debugging
        if stage == 3:  # This statement adds a 3rd coord to the existing 2
            # print("..")  # Only for debugging
            if position(coordinates) == "horizontal":  # If coord1 and coord2 are in the same row
                if coord1IsOnWhatSideOfCoord2(coordinates) == "right":  # If coord1 is on the right of coord2
                    coordinates.append(letter(coordinates)
                                              + (str(int(coordinates[0][1]) - 2))
                                              )
                elif coord1IsOnWhatSideOfCoord2(coordinates) == "left":  # If coord1 is on the left of coord2
                    coordinates.append(coordinates[0][0]
                                              + (str(int(coordinates[0][1]) + 2))
                                              )
                    # print("...")  # Only for debugging
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
        # except IndexError:
        #    coordinates = False
        #    return coordinates
    # print("???")  # Only for debugging

def collectCoordsNearShip(stage, coordsOfShip, coordsNearShips):

    from commonFunctions import letter, letterAbove, letterBelow
    from commonFunctions import number, numberNext, numberPrev
    from commonFunctions import position, rowsBeside, columnsBeside, isReverse, letters

    # global coordsNearShips1  # Only for debugging
    # global coordsNearShips2  # Only for debugging

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
def coordInputCheck(stage, player, seafield):  # coordInputCheck!!!!!!!!!!!!!!!!!!!
    from commonFunctions import isInputValid
    if player == "Player 1":
        global coordsNearShip1
        coordsNearShip = coordsNearShip1
    elif player == "Player 2":
        global coordsNearShip2
        coordsNearShip = coordsNearShip2
    good_coordinates = []
    while True:
        coordInput = input(cyan + "\n\n" + player + "! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: "+default)
        coordInput = coordInput.split()
        if coordInput == ["q"]:
            return "q"
        if len(coordInput) != 1:
            # if isInputValid(stage, player1_shcoordInputip_place, seafield) == True:
            coordInput = new_placing(coordInput, stage, seafield)
            # print(coordInput)  # Only for debugging
        if type(coordInput) != bool:
            # print(player)  # Only for debugging
            try:
                if len(coordInput) >= 1:
                    # print(player)  # Only for debugging
                    if isInputValid(coordInput, seafield, stage) == True:
                        # print(player)  # Only for debugging
                        # print("len of... ", len(coordInput))  # Only for debugging
                        collectCoordsNearShip(stage, coordInput, coordsNearShip)
                        # print(coordsNearShip)  # Only for debugging
                        for ship in coordInput:
                            # print(player, "...")  # Only for debugging
                            for coordinate in seafield:
                                if ship == coordinate and coordinate != "OO" and ship not in coordsNearShip:
                                    good_coordinates.append("1")
                                    # print(good_coordinates)  # Only for debugging
            except TypeError:
                pass
        # print(good_coordinates)   # Only for debugging
        if len(good_coordinates) == stage:
            return coordInput
        else:
            print("Wrong format or reserved place, try again!")
            good_coordinates = []
            if type(coordInput) != bool:
                if isInputValid(coordInput, player_1_seafield, stage) == True:
                    wrongCoords = []
                    collectCoordsNearShip(stage, coordInput, wrongCoords)
                    for coordinate in wrongCoords:
                        coordsNearShip.remove(coordinate)


# Changes the checked coordinates to "OO" in the seafield
def insert_input(seafield, shipplace):
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


def menu_func(menu, exit):

    cleaning()

    pause = True

    while pause is True:

        menu = input(bold+whitebgblack+"\nBATTLESHIP GAME by Sano and Zoli"
                     + "\n\n" + "Press q to exit"
                     + "\n" + "Press m to see manual"
                     + "\n" + "Press s to start game "
                     + "\n" + "Press l to load game "
                     + "\n" + "Press sv to save game "
                     + '\033[0m'
                     )

        if menu == "q":  # BUG need to be implemented
            exit = True
            return menu, exit

        elif menu == "m":
            with open(fileDir + "/README.md") as manual:
                manual = manual.read()
                print(manual)
            continue

        elif menu == "l":
            return menu, exit

        elif menu == "s":
            return menu, exit

        elif menu == "sv":
            saving()

        cleaning()


def placing():
    global player_1_placing_counter
    global player_2_placing_counter
    global placing_turns
    while player_1_placing_counter <= placing_turns:
        insert_input(player_1_seafield, coordInputCheck(player_1_placing_counter, "Player 1", player_1_seafield))
        if menu == "q":
            # print(coordsNearShips1)  # Only for debugging
            # print(coordsNearShips2)  # Only for debugging
            # input("Press enter to continue ")
            return
        player_1_placing_counter += 1
    cleaning()
    while player_2_placing_counter <= placing_turns:
        insert_input(player_2_seafield, coordInputCheck(player_2_placing_counter, "Player 2", player_2_seafield))
        if menu == "q":
            return
        player_2_placing_counter += 1
    cleaning()


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
                if player == "Player 1":
                    player_1_hits += 1
                elif player == "Player 2":
                    player_2_hits += 1
                break


# Checks...
def striking_check(strikes, player):
    good_coordinates = []
    while True:
        new_strike = input(player + " , please give a coordinate to strike: ")
        if new_strike == "q":
            return "q"
        for strike in strikes:
            if new_strike == strike and strike != "OO" and strike != "xx":    
                good_coordinates.append("1")
        if len(good_coordinates) == 1:
            return new_strike
        else:
            print("Wrong format or reserved place, try again!")


def strike_input(player):
    if player == "Player 1":
        global player_1_strike_counter
        strikes = player_1_strikes
        seafield = player_1_seafield
    if player == "Player 2":
        global player_2_strike_counter
        strikes = player_2_strikes
        seafield = player_2_seafield
    print_field(strikes)
    # print(player_1_hits, player_1_strike_counter)  # Only for debugging
    # print(player_2_hits, player_2_strike_counter)  # Only for debugging
    striking_function(player, strikes, striking_check(strikes, player), seafield)
    if menu == "q":
        return
    if player == "Player 1":
        player_1_strike_counter += 1
    elif player == "Player 2":
        player_2_strike_counter += 1
    cleaning()


def gameplay():

    global player_1_hits
    global player_2_hits
    global player_1_strike_counter
    global player_2_strike_counter
    global maxHits

    cleaning()

    if menu == "q":
        return

    placing()

    if menu == "q":
        return

    while player_1_hits < maxHits and player_2_hits < maxHits:
        if player_1_strike_counter <= player_2_strike_counter:
            strike_input("Player 1")
            if menu == "q":
                return
        else:
            strike_input("Player 2")
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


# TO BE MAIN
cleaning()
menu = ""
exit = False


while exit is False:
    menu, exit = menu_func(menu, exit)
    if menu != "q":
        placing_turns = 0
        player_1_placing_counter = 1
        player_2_placing_counter = 1
        player_1_strike_counter = 0
        player_2_strike_counter = 0
        player_1_hits = 0
        player_2_hits = 0
        maxHits = 0
        coordsNearShip1 = []
        coordsNearShip2 = []

        if menu == "s":
            seafield = loading("new", fileDir + "/battleShipSeafield")
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
                        x = True

        elif menu == "l":
            seafield = loading("saved",  fileDir + "/battleShipSavedGame")
            player_1_placing_counter = int(seafield[4])
            player_2_placing_counter = int(seafield[5])
            placing_turns = int(seafield[6])
            player_1_hits = int(seafield[7])
            player_2_hits = int(seafield[8])
            player_1_strike_counter = int(seafield[9])
            player_2_strike_counter = int(seafield[10])
            coordsNearShip1 = seafield[11]
            coordsNearShip2 = seafield[12]
            # print(coordsNearShips1)  # Only for debugging
            # print(coordsNearShips2)  # Only for debugging
            # a = input("press enter to continue")  # Only for debugging

        player_1_seafield = seafield[0]
        player_1_strikes = seafield[1]
        player_2_seafield = seafield[2]
        player_2_strikes = seafield[3]
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