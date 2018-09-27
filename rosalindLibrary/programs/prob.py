#-------------------------------------------------------------------------------
# Needed libraries
#-------------------------------------------------------------------------------
from math import log10
#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------
def runProb(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    dnaString = fi.readline() #reads in files
    percents = fi.readline().split(" ")

    #calculating GC content and percent
    GCcont = 0.0
    for k in dnaString:
        if (k == "G") or (k == "C"):
            GCcont += 1.0
    GCpercent = len(dnaString) / GCcont

    results = []

    for k in percents:
        totalDnaChance = 1.0
        atPercent = (1.0 - float(k)) * 0.5
        gcPercent = float(k) * 0.5

        for i in dnaString:
            if (i == "A") or (i == "T"):
                totalDnaChance = totalDnaChance * atPercent
            if (i == "C") or (i == "G"):
                totalDnaChance = totalDnaChance * gcPercent
        results.append(str(round(log10(totalDnaChance), 3)))


    return " ".join(results)

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
