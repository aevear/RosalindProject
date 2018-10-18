#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------

def runLong(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    inLoop, assembledArray, convergentString = True, [], fastaData[0]

    for k in fastaData:
        assembledArray.append(0)

    assembledArray[0] = 1

    while inLoop:
        for index, dnaSnips in enumerate(fastaData):
            if dnaSnips in convergentString:
                assembledArray[index] = 1
            elif assembledArray[index] == 0:
                #Front end checking
                for snpIndex in range(len(fastaData[0])/2):
                    if dnaSnips[snpIndex:] == convergentString[:len(dnaSnips)-snpIndex]:
                        convergentString = dnaSnips[:snpIndex] + convergentString
                        assembledArray[index] = 1
                for snpIndex in range(len(fastaData[0])/2):
                    if dnaSnips[:-snpIndex] == convergentString[-len(dnaSnips)+snpIndex:]:
                        convergentString = convergentString + dnaSnips[-snpIndex:]
                        assembledArray[index] = 1

        if 0 not in assembledArray:
            inLoop = False
    return convergentString

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
