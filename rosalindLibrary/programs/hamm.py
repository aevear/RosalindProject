#-------------------------------------------------------------------------------
# Hamm
#-------------------------------------------------------------------------------
def runHamm(inputFile):
    fi = open(inputFile, "r")
    sourceLine, deviantLine = fi.readline(), fi.readline()
    hammDistance = 0

    if len(sourceLine) != len(deviantLine):
        return "The lengths are not the same"

    for k in range(len(sourceLine)):
        if sourceLine[k] != deviantLine[k]:
            hammDistance +=1

    return hammDistance
#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
