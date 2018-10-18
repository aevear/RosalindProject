#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
from itertools import permutations
#-------------------------------------------------------------------------------
# Pmch
#-------------------------------------------------------------------------------
def permutationEngine(inputData):
    combinations = []
    for k in range(int(inputData)):
        combinations.append(k)
    perm = list(permutations(combinations))
    return len(perm)


def runPmch(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    GC, UA = 0, 0

    for k in fastaData[0]:
        if k == "U":
            UA += 1
        if k == "G":
            GC += 1

    return permutationEngine(GC) * permutationEngine(UA)

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
