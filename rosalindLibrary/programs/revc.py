#-------------------------------------------------------------------------------
# Revc
#-------------------------------------------------------------------------------

def runRevc(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    activityFile = fi.read() #reads in files
    finalString = ""

    for k in activityFile:
        if k =="T":
            finalString = finalString + "A"
        if k =="A":
            finalString = finalString + "T"
        if k =="G":
            finalString = finalString + "C"
        if k =="C":
            finalString = finalString + "G"

    finalString = finalString[::-1]

    return finalString

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
