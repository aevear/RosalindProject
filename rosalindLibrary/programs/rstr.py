#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------

def runGc(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)

    winner, highest, gcContent, counter = 0, 0.0, 0.0, 0
    for fastaEntry in fastaData:
        for nucleotide in fastaEntry:
            if (nucleotide == "G" or nucleotide == "C"):
                gcContent += 1
        if (gcContent/len(fastaEntry)) > highest:
            highest = gcContent/len(fastaEntry)
            winner = counter
        gcContent = 0.0
        counter += 1
    highest = highest * 100

    return (fastaNames[winner] + "\n" + str(round(highest, 6)))

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
