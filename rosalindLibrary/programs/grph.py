#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# Grph
#-------------------------------------------------------------------------------

def runGrph(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    front03, back03, results = [], [], []

    #make front and back 03
    for k in fastaData:
        front03.append(k[:3])
        back03.append(k[-3:])

    for frontCounter, frontEnd in enumerate(front03):
        for backCounter, backEnd in enumerate(back03):
            if frontCounter != backCounter:
                if frontEnd == backEnd:
                    results.append(fastaNames[backCounter] + " " + fastaNames[frontCounter])

    return "\n".join(results)

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
