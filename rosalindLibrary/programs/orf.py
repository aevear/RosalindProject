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
    #Bua this is going to be terrible, but I am going to just do the same thing and reverse it. Lame but well, it'll work
    for index in range(len( fastaData[0] ) -2 ):
        if (fastaData[0][index] == "A") and (fastaData[0][index+1] == "T") and (fastaData[0][index+2] == "G"):
            openFrameLocations.append(index)

    for index in openFrameLocations:
        tempResults = findProteins(index, fastaData[0])
        if tempResults != 1:
            results.append(tempResults)


    #Ok here we are going to reverse it kkkkk
    reverseString, inverseString = fastaData[0][::-1], ""
    for k in reverseString:
        if k == "A":
            inverseString += "T"
        elif k == "T":
            inverseString += "A"
        elif k == "C":
            inverseString += "G"
        elif k == "G":
            inverseString += "C"

    for index in range(len( inverseString ) -2 ):
        if (inverseString[index] == "A") and (inverseString[index+1] == "T") and (inverseString[index+2] == "G"):
            reverseFrameLocations.append(index)

    for index in reverseFrameLocations:
        tempResults = findProteins(index, inverseString)
        if tempResults != 1:
            results.append(tempResults)


    return list(set(results))
#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
