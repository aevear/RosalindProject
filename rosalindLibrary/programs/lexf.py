#-------------------------------------------------------------------------------
# Lexf
#-------------------------------------------------------------------------------

def runLexf(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    variables = fi.readline().replace(" ", "").strip("\n") #reads in files
    length = fi.readline().strip()

    results = []

    import itertools
    results = list(itertools.product(variables, repeat=int(length)))

    results = '\n'.join(map(str, results))

    return results.replace('\'', "").replace('(', "").replace(")", "").replace(", ", "")




#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
