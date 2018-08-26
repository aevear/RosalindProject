#-------------------------------------------------------------------------------
# Revc
#-------------------------------------------------------------------------------

def runFib(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    activityFile = fi.readline().split() #reads in files
    n, m = int(activityFile[0]), int(activityFile[1])

    sequence = list()
    mature, immature, babies = 0, 1, 0

    for i in range(n-1):
        #Make Babies
        newbabies = mature * m
        mature = immature + mature
        immature = newbabies
        total = mature + immature + babies
    return total


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
