#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# Cons
#-------------------------------------------------------------------------------
def runCons(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    consensusArray, results = [], ""

    #creates a blank array for each letter the length of the row
    for k in range(4):
        consensusArray.append([])
        for i in fastaData[0]:#This creates the length of the array
            consensusArray[k].append(0)

    #ACtually go thorugh and make the array
    for line in fastaData:
        for index, char in enumerate(line):
            if char == "A":
                consensusArray[0][index] += 1
            if char == "C":
                consensusArray[1][index] += 1
            if char == "G":
                consensusArray[2][index] += 1
            if char == "T":
                consensusArray[3][index] += 1


    #turns it into something actually useful to present rather than a big ol list
    nucliotides = ["A", "C", "G", "T"]
    for index, k in enumerate(nucliotides):
        results = results + k + ":"
        for i in consensusArray[index]:
            results = results + " " + str(i)
        results = results + "\n"

    return results

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
