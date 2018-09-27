#-------------------------------------------------------------------------------
# Revc
#-------------------------------------------------------------------------------

def rosalindLoader(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputFile = fi.read().replace('\n', '').split(">") #reads in files
    fastaData, fastaNames = [], []

    for inputLine in inputFile:
        fastaName = ""
        fastaString = ""

        for char in inputLine:
            if (char == "A") or (char == "C") or (char == "G") or (char == "T"):
                fastaString = fastaString + char
            else:
                fastaName = fastaName + char

        fastaNames.append(fastaName)
        fastaData.append(fastaString)

    return fastaNames[1:], fastaData[1:]


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
