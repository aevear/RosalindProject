#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------

def runIev(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.read().strip("\n").split(" ") #reads in files
    aaaa, aaab, aabb, abab, abbb, bbbb = float(inputData[0]), float(inputData[1]), float(inputData[2]), float(inputData[3]), float(inputData[4]), float(inputData[5])
    totalDominatOffspring = 0.0

    #Add up each probability
    totalDominatOffspring = (((aaaa + aaab + aabb) * 1) + (abab * 0.75) + (abbb * .5) + (bbbb * 0)) * 2

    return totalDominatOffspring



#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
