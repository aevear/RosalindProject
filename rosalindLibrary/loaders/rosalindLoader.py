#-------------------------------------------------------------------------------
# Revc
#-------------------------------------------------------------------------------

def rosalindLoader(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputFile = fi.read().replace('\n', '').split(">") #reads in files
    fastaData, fastaNames = [], []

    for k in inputFile:
        fastaNames.append(k[:13])
        fastaData.append(k[13:])

    return fastaNames[1:], fastaData[1:]


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
