#-------------------------------------------------------------------------------
# Subs
#-------------------------------------------------------------------------------

def runSubs(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    sourceString = fi.readline() #reads in files
    referenceString = fi.readline() #reads in files

    referenceString = referenceString.strip()

    location, results = 0, ""

    for k in sourceString[:-len(referenceString)]:
        if k == referenceString[0]:
            if (sourceString[location:(location + len(referenceString))]) == referenceString:
                results = results + " " + str(location +1)
        location += 1

    return results[1:]


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
