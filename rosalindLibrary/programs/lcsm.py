#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# Lcsm
#-------------------------------------------------------------------------------

def runLcsm(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    fastaData = sorted(fastaData)
    template = fastaData[0]
    min_length = len(fastaData[0])
    longestMatch = ""

    for i in range(0, min_length):
        for j in range(min_length, i + len(longestMatch), -1):
            s1 = template[i:j]

            matched_all = True
            for s2 in fastaData[1:]:
                if s1 not in s2:
                    matched_all = False
                    break

            if matched_all:
                longestMatch = s1
                break

    return longestMatch

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
