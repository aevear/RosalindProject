#-------------------------------------------------------------------------------
# DNA
#-------------------------------------------------------------------------------

def runDna(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.read() #reads in files
    aCount, gCount, tCount, cCount = 0, 0, 0, 0

    for k in inputData:
        if k =="A":
            aCount +=1
        if k =="G":
            gCount +=1
        if k =="T":
            tCount +=1
        if k =="C":
            cCount +=1

    return str(aCount) + " " + str(cCount) + " " + str(gCount) + " " + str(tCount)

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
