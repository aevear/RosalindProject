#-------------------------------------------------------------------------------
# Lgis
#-------------------------------------------------------------------------------
def runLgis(inputFile):
    fi = open(inputFile, 'r')
    inputData, permArray = fi.readline(), fi.readline().strip("\n").split(" ")
    highestPath, lowestPath = [], []

    #to find highest path
    for index, k1 in enumerate(permArray):
        tempHigh = [k1]
        print "yuhuuu" + str(tempHigh)
        for k2 in permArray[index:]:
            print k2 + " : " + str(int(tempHigh[-1]) + 1)
            if k2 == str(int(tempHigh[-1]) + 1):
                tempHigh.append(k2)
        if len(tempHigh) > len(highestPath):
            highestPath = tempHigh

    #to find lowest path


    return highestPath


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
