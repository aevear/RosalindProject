#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
from rosalindLibrary.tools.rosalindTools import nucToProtien
#-------------------------------------------------------------------------------
# Orf
#-------------------------------------------------------------------------------
def findProteins(index, dnaString):
    protienString, looping = "", True
    readingFrame = index
    while looping:
        if (len(dnaString) - readingFrame ) < 3:
            looping = False
        else:
            newProtien = nucToProtien(dnaString[readingFrame:readingFrame+3])
            if newProtien == "Stop":
                looping = False
                return protienString
            else:
                protienString = protienString + newProtien
                #print protienString
                readingFrame +=3
    return 1


def runOrf(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    openFrameLocations, reverseFrameLocations, results = [], [], []

    #This part will make a list of all open reading frames that will be fed to the next part and exaimed there
    for index in range(len( fastaData[0] ) -2 ):
        if (fastaData[0][index] == "A") and (fastaData[0][index+1] == "T") and (fastaData[0][index+2] == "G"):
            openFrameLocations.append(index)
        if (fastaData[0][index] == "C") and (fastaData[0][index+1] == "A") and (fastaData[0][index+2] == "T"):
            reverseFrameLocations.append(index)

    for index in openFrameLocations:
        tempResults = findProteins(index, fastaData[0])
        print tempResults
        if tempResults != 1:
            results.append(tempResults)

    return results
#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
