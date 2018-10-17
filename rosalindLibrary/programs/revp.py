#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------
def inverse(givenString):
    givenString = givenString[::-1]
    result = ""
    for k in givenString:
        if k == "A":
            result += "T"
        if k == "T":
            result += "A"
        if k == "C":
            result += "G"
        if k == "G":
            result += "C"
    return result


def runRevp(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    dnaString = fastaData[0] + "             "
    result = ""

    for index in range(len(dnaString)):
        #check length 4
        if dnaString[index:index+2] == inverse(dnaString[index+2:index+4]):
            result+= str(index+1) + " 4\n"
        #check length 6
        if dnaString[index:index+3] == inverse(dnaString[index+3:index+6]):
            result+= str(index+1) + " 6\n"
        #check length 8
        if dnaString[index:index+4] == inverse(dnaString[index+4:index+8]):
            result+= str(index+1) + " 8\n"
        #check length 10
        if dnaString[index:index+5] == inverse(dnaString[index+5:index+10]):
            result+= str(index+1) + " 10\n"
        #check length 12
        if dnaString[index:index+6] == inverse(dnaString[index+6:index+12]):
            result+= str(index+1) + " 12\n"



    return result

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
