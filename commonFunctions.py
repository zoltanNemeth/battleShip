letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def letter(coordinates, index=0):
    letter = coordinates[index][0]
    return letter

def letterAbove(coordinate):
    if coordinate[0] != "a":
        letterAbove = letters[letters.index(coordinate[0]) - 1]  # BUG coord jx added in case of ax
    else:
        letterAbove = "x"
    return letterAbove

def letterBelow(coordinate):
    try:
        letterBelow = letters[letters.index(coordinate[0]) + 1]  # BUG IndexError (out of range)
    except IndexError:
        letterBelow = "x"
    return letterBelow

def number(coordinates, index=0, oneCoord=False):
    if len(coordinates[index]) == 3:
        number = "10"
    elif oneCoord is True:
        if len(coordinates) == 3:
            number = "10"
        else:
            number = coordinates[1]
    else:
        number = coordinates[index][1]
    return number

def numberNext(coordinate):
    if len(coordinate) == 3:
        numberNext = "0"
    else:
        numberNext = str(int(coordinate[1]) + 1)  # small BUG can give coord x10? unnecessarily
    return numberNext

def numberPrev(coordinate):
    if len(coordinate) == 3:
        numberPrev = "9"
    else:
        numberPrev = str(int(coordinate[1]) - 1)  # small BUG can give coord x0 unnecessarily
    return numberPrev

def position(coordsOfShip):
    if coordsOfShip[0][0] == coordsOfShip[-1][0]:
        return "horizontal"
    else:
        return "vertical"

def coord1IsOnWhatSideOfCoord2(coordsOfShip):
    if number(coordsOfShip) == str(int(number(coordsOfShip, 1)) + 1):
        coord1IsOnWhatSideOfCoord2 = "right"
        return coord1IsOnWhatSideOfCoord2
    elif number(coordsOfShip) == str(int(number(coordsOfShip, 1)) - 1):
        coord1IsOnWhatSideOfCoord2 = "left"
        return coord1IsOnWhatSideOfCoord2
    else:
        return

def isReverse(coordsOfShip):
    if position(coordsOfShip) == "horizontal":
        if int(number(coordsOfShip)) > int(number(coordsOfShip, -1)):
            return True
        else:
            return False
    else:  # If vertical
        if letters.index(letter(coordsOfShip)) > letters.index(letter(coordsOfShip, -1)):
            return True
        else:
            return False

def rowsBeside(coordsOfShip, coordsNearShip):  # IF HORIZONTAL!
    for coordinate in coordsOfShip:  # Add to coordsNearShip the row above and below of the ship
        if letter != "a":
            coordsNearShip.append(
                letterAbove(coordinate)
                + number(coordinate, oneCoord=True)
            )
        if letter != "j":
            coordsNearShip.append(
                letterBelow(coordinate)
                + number(coordinate, oneCoord=True)
            )

def columnsBeside(coordsOfShip, coordsNearShip):  # IF HORIZONTAL!
    if isReverse(coordsOfShip) is True:
        leftEnd = letter(coordsOfShip, -1) + numberPrev(coordsOfShip[-1])
        rightEnd = letter(coordsOfShip) + numberNext(coordsOfShip[0])
    else:
        leftEnd = letter(coordsOfShip) + numberPrev(coordsOfShip[0])
        rightEnd = letter(coordsOfShip, -1) + numberNext(coordsOfShip[-1])
        # print(leftEnd)  # Only for debugging
        # print(rightEnd)  # Only for debugging
    coordsNearShip.extend(  # Add to coordsNearShip the column on the left of the ship
            [
            letterAbove(leftEnd) + number(leftEnd, oneCoord=True),
            leftEnd,
            letterBelow(leftEnd) + number(leftEnd, oneCoord=True)
            ]
    )
    coordsNearShip.extend(  # Add to coordsNearShip the column on the right of the ship
        [
        letterAbove(rightEnd) + number(rightEnd, oneCoord=True),
        rightEnd,
        letterBelow(rightEnd) + number(rightEnd, oneCoord=True)
        ]
    )

def isInputValid(stage, input, seafield):
    try:
        good_coordinates = 0
        for item in input:
            for coordinate in seafield:
                if item == coordinate and coordinate != "OO":
                        good_coordinates += 1
        if good_coordinates == len(input) and stage == len(input):
            return True
        else:
            return False
    except TypeError:
        return False