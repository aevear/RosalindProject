#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------
def runProb(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    dnaString = fi.readline() #reads in files
    percents = fi.readline().split(" ")

    GCcont = 0.0
    for k in dnaString:
        if (k == "G") or (k == "C"):
            GCcont += 1
    GCpercent = len(dnaString) / GCcont












    return GCpercent

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
