#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------

def runSseq(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    s, t = fastaData[0], fastaData[1]
    stringPosition, results = -1, []

    for k in t:
        stringPosition += s.index(k) + 2
        results.append(stringPosition)
        s = s[s.index(k)+2::]

    return ' '.join(map(str, results))




#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
