#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.tools.rosalindTools import monoisotopicTable
#-------------------------------------------------------------------------------
# Prtm
#-------------------------------------------------------------------------------
def runPrtm(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.readline().strip() #reads in files
    total = 0.0

    for k in inputData:
        total = total + monoisotopicTable(k)


    return total

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
