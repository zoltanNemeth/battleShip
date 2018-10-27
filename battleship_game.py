import sys

# FUNCTIONS:

def print_field(field):
    print("\nYour choices:")
    for i in field:       
        if i == "\n":
            print(i, end="") 
        else:
            print(i, end=" ")

def cleaning():
    sys.stdout.write("\033[2J")
    #sys.stdout.write("\033[<20>A")
    sys.stdout.flush()

def player_1_ship_place(stage):
    good_coordinates = []
    while True:
        player1_ship_place = input("\n\nPlayer 1! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: ")
        player1_ship_place = player1_ship_place.split()
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
        player2_ship_place = input("\n\nPlayer 2! Add coordinate(s) for the " + str(stage) + " coordinate-long ship: ")
        player2_ship_place = player2_ship_place.split() 
        for ship in player2_ship_place:
            for seafield in player_2_seafield:
                if ship == seafield and seafield != "OO":    
                    good_coordinates.append("1")
        if len(good_coordinates) == stage:
            return  player2_ship_place
        else:
            print("Wrong format or reserved place, try again!")
            good_coordinates = []

def ship_placing(seafield, shipplace):    
    for i in seafield:
        index = seafield.index(i)
        for i in shipplace:
            index2 = shipplace.index(i)
            if seafield[index] == shipplace[index2]:
                del seafield[index]
                seafield.insert(index, "OO")
    print_field(seafield)

def striking_function(hits, strikes, strike, seafield):
        for i in strikes:
            index_of_list = strikes.index(i) 
            if strikes[index_of_list] == strike:
                del strikes[index_of_list]
                strikes.insert(index_of_list, "xx")
                if seafield[index_of_list] == "OO":
                    strikes.insert(index_of_list, "OO")
                    del strikes[index_of_list + 1]
                    hits.append("1")
                    break              
        print_field(player_1_strikes)

def striking_check(strikes, player):
    good_coordinates = []
    while True:
        player_1_strike = input("\n\nPlayer " + str(player) + ", please give a coordinate to strike: ")
        for strike in strikes:
            if player_1_strike == strike and strike != "OO" and strike != "xx":    
                good_coordinates.append("1")
        if len(good_coordinates) == 1:
            return  player_1_strike
        else:
            print("Wrong format or reserved place, try again!")

# "MAIN()"

while True:

    menu = input("\nBATTLESHIP GAME by Sano and Zoli" + "\n\n" + "Press q to exit" + "\n" + "Press m to see manual" + "\n" + "Press s to start game ")

    if menu == "q":
        break

    elif menu == "m":
        print("\nThe size of the seafield is 10X10, use letters (rows) and numbers (columns) to enter the coordinates, e.g.: a1 a2")
        continue

    elif menu == "s":
        player_1_seafield = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "\n" , "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "\n", "c1","c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "\n", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "\n", "e1", "e2" , "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "\n", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", '\n', "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "\n", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "\n", "i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10", "\n", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10"]
        player_1_strikes = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "\n" , "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "\n", "c1","c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "\n", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "\n", "e1", "e2" , "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "\n", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", '\n', "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "\n", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "\n", "i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10", "\n", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10"]
        player_1_hits = []

        player_2_seafield = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "\n" , "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "\n", "c1","c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "\n", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "\n", "e1", "e2" , "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "\n", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", '\n', "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "\n", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "\n", "i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10", "\n", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10"]
        player_2_strikes = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "\n" , "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "\n", "c1","c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "\n", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "\n", "e1", "e2" , "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "\n", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", '\n', "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "\n", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "\n", "i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10", "\n", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j10"]
        player_2_hits = []    

        cleaning()

        x = 1

        while x < 4:
            ship_placing(player_1_seafield, player_1_ship_place(x))
            x += 1

        cleaning()
        x = 1

        while x < 4:
            ship_placing(player_2_seafield, player_2_ship_place(x))
            x += 1
       
        cleaning()

        while len(player_1_hits) < 2 and len(player_2_hits) < 2:
            print_field(player_1_strikes)
            striking_function(player_1_hits, player_1_strikes, striking_check(player_1_strikes, 1), player_2_seafield)
            cleaning()
            if len(player_1_hits) < 2 and len(player_2_hits) < 2:
                print_field(player_2_strikes)
                striking_function(player_2_hits, player_2_strikes, striking_check(player_2_strikes, 2), player_1_seafield)
                cleaning()    

        if player_2_hits > player_1_hits:
            print("\n\n" + "Player 2 won")
            print_field(player_2_strikes)
            break
        else:
            print("\n\n" + "Player 1 won")
            print_field(player_1_strikes)
            break