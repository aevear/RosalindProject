#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from itertools import permutations
#-------------------------------------------------------------------------------
# Perm
#-------------------------------------------------------------------------------
def runPerm(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.read() #reads in files

    #generate factorial
    combinations, results = [], ""
    for k in range(int(inputData)+1):
        combinations.append(k)

    perm = permutations(combinations[1:])

    # Print the obtained permutations
    length = 0
    for i in list(perm):
        results = results + str(i)
        length +=1

    results = results.replace("(", "\n").replace(")", "").replace(",", "")

    return str(length) + "\n" + results[1:]

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
