#-------------------------------------------------------------------------------
# Revc
#-------------------------------------------------------------------------------

def runFib(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.readline().split() #reads in files
    n, m = int(inputData[0]), int(inputData[1])

    mature, immature = 0, 1

    for i in range(n-1):
        newbabies = mature * m
        mature = immature + mature
        immature = newbabies
        total = mature + immature
    return total


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
