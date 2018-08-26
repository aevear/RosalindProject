#-------------------------------------------------------------------------------
# DNA
#-------------------------------------------------------------------------------

def runRna(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    activityFile = fi.read() #reads in files
    finalString = ""

    for k in activityFile:
        if k =="T":
            finalString = finalString + "U"
        else:
            finalString = finalString + k


    return finalString

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
