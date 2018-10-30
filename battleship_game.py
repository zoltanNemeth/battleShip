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


def print_field(field):
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


def cleaning():
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
                        )


def loading(filename="/home/nemethzoltan/Desktop/battleShip/battleShipSavedGame"):
    with open(filename, "r") as savedFile:
        data = savedFile.read()
        data = data.split("p")
        data = [data[0].split(","),
                data[1].split(","),
                data[2].split(","),
                data[3].split(",")
               ]
        return data


def player_1_ship_place(stage):
    good_coordinates = []
    while True:
        player1_ship_place = input(cyan+"\n\nPlayer 1! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: "+default)
        player1_ship_place = player1_ship_place.split()
        if player1_ship_place == ["q"]:
            return "q"
        for ship in player1_ship_place:
            for seafield in player_1_seafield:
                if ship == seafield and seafield != "OO":    
                    good_coordinates.append("1")
        if len(good_coordinates) == stage:
            return  player1_ship_place
        else:
            print("Wrong format or reserved place, try again!")
            good_coordinates = []


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


def striking_function(hits, strikes, strike, seafield):
    if strike == "q":
        global menu
        menu = "q"
        return "q"
    for i in strikes:
        index_of_list = strikes.index(i) 
        if strikes[index_of_list] == strike:
            del strikes[index_of_list]
            strikes.insert(index_of_list, "xx")
            if seafield[index_of_list] == "OO":
                strikes.insert(index_of_list, "@@")
                del strikes[index_of_list + 1]
                hits.append("1")
                break


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

    player_1_hits = []
    player_2_hits = []
    cleaning()

    def placing():
        x = 1
        while x < 4:
            ship_placing(player_1_seafield, player_1_ship_place(x))
            if menu == "q":
                return
            x += 1
        cleaning()
        x = 1
        while x < 4:
            ship_placing(player_2_seafield, player_2_ship_place(x))
            if menu == "q":
                return
            x += 1
        cleaning()

    def battle():
        while len(player_1_hits) < 2 and len(player_2_hits) < 2:
            print_field(player_1_strikes)
            striking_function(player_1_hits, player_1_strikes, striking_check(player_1_strikes, 1), player_2_seafield)
            if menu == "q":
                return
            cleaning()
            if len(player_1_hits) < 2 and len(player_2_hits) < 2:
                print_field(player_2_strikes)
                striking_function(player_2_hits, player_2_strikes, striking_check(player_2_strikes, 2), player_1_seafield)
                if menu == "q":
                    return
                cleaning()
    
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
    if menu == "s":
        seafield = loading("/home/nemethzoltan/Desktop/battleShip/battleShipSeafield")
        return
    elif menu == "l":
        seafield = loading("/home/nemethzoltan/Desktop/battleShip/battleShipSavedGame")
        return


# TO BE MAIN
cleaning()
menu = ""
exit = False
loadedPhase = ""

while exit == False:
    menu_func()
    loadedPhase = ""
    if menu != "q":
        seafield = []
        seafield_func()
        player_1_seafield = seafield[0]
        player_1_strikes = seafield[1]
        player_2_seafield = seafield[2]
        player_2_strikes = seafield[3]
        if "xx" in player_1_strikes or "xx" in player_2_strikes or "@@" in player_1_strikes or "@@" in player_2_strikes:
            loadedPhase = "battle"
        gameplay()