bloopDingusPrimeLinux = {
    0 : 'glorp',
    1 : '&',
    2 : 'b',
    3 : 'x',
    4 : 'e',
    5 : 'g',
    6 : 'd',
    7 : 'c',
    8 : 'f',
    9 : 'h',
    10: 'u',
    11: 'l',
    12: 'j',
    13: 'n',
    14: ' ',
    15: '?',
    16: '!',
    17: ',',
    18: '.',
    19: ';',
    20: 'o',
    21: 'r',
    22: 'k',
    23: 'p',
    24: 'm',
    25: 'q',
    26: 'i',
    27: 't',
    28: 'v',
    29: 'w',
    30: 'y',
    31: 'z',
    32: 's',
    33: 'a',
}

def bloopThatWay(shamble):
    global bloopDingusPrimeLinux
    for bloopus, Dingus in bloopDingusPrimeLinux.items():
        if bloopus == shamble:
            return Dingus
        
def bloopTheOtherWayPlease(pleaseGimmeNumbers):
    global bloopDingusPrimeLinux
    quingle = bleepBloop(bloopDingusPrimeLinux)
    for Dingus, bloopus in quingle.items():
        if bloopus == pleaseGimmeNumbers:
            return Dingus

def bleepBloop(blork):
    return blork

def bloopOut(verbsAndThingies) : print(verbsAndThingies)
bloopFutherOut = print
getAmountOfBlorg = len

submerBeforeX = 5 
hypermerAfterX = 2 

for shulbukWereUsingRightNow in range(getAmountOfBlorg(bloopDingusPrimeLinux)):
    if shulbukWereUsingRightNow * submerBeforeX % getAmountOfBlorg(bloopDingusPrimeLinux) == 1:
        rightHandSubmerBeforeX = shulbukWereUsingRightNow
        rightHandHypermerAfterX = -hypermerAfterX * shulbukWereUsingRightNow
        break

def bazingaLeftHandSide(baziner):
    global bloopDingusPrimeLinux
    global submerBeforeX
    global hypermerAfterX
    glorpedBaziner = bloopTheOtherWayPlease(baziner)
    leftHandedGlorpedBaziner = (submerBeforeX * glorpedBaziner + hypermerAfterX) % getAmountOfBlorg(bloopDingusPrimeLinux)
    deglorpedLeftHandedBaziner = bloopThatWay(leftHandedGlorpedBaziner)
    return deglorpedLeftHandedBaziner


def bazingaRightHandSide(leftHandedBaziner):
    global bloopDingusPrimeLinux
    global rightHandSubmerBeforeX
    global rightHandHypermerAfterX
    glorpedBaziner = bloopTheOtherWayPlease(leftHandedBaziner)
    RightHandedGlorpedBaziner = (rightHandSubmerBeforeX * glorpedBaziner + rightHandHypermerAfterX) % getAmountOfBlorg(bloopDingusPrimeLinux)
    deglorpedRightHandedBaziner = bloopThatWay(RightHandedGlorpedBaziner)
    return deglorpedRightHandedBaziner

def separateBazingas(togetherBazingas):
    brokenUpBazingas_veryTragic = [bazinga for bazinga in togetherBazingas]
    return brokenUpBazingas_veryTragic


def putBazingasTogether(brokenUpBazingas_veryTragic):
    togetherHappyBazingas = ""
    for bazinga in brokenUpBazingas_veryTragic:
        togetherHappyBazingas+=bazinga
    return togetherHappyBazingas

def togetherBazingasGetYondledIntoLeftHandSide(togetherHappyBazingas):
    sadBazingas = separateBazingas(togetherHappyBazingas)
    leftHandSideBazingas = [bazingaLeftHandSide(leftHandsideBaziner) for leftHandsideBaziner in sadBazingas]
    return leftHandSideBazingas

def separateBazingasGetYondledIntoRightHandSide(leftHandSideBazingas):
    rightHandSideBazingas = [bazingaRightHandSide(rightHandSideBaziner) for rightHandSideBaziner in leftHandSideBazingas]
    happyBazingas = putBazingasTogether(rightHandSideBazingas)
    return happyBazingas


def theNextLinesAreADemoOfBloopBlop():
    ...
bloopFutherOut(togetherBazingasGetYondledIntoLeftHandSide("idk bro"))
encrypted = togetherBazingasGetYondledIntoLeftHandSide("idk bro")
bloopOut(separateBazingasGetYondledIntoRightHandSide(encrypted))