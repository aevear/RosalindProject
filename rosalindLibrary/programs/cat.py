#-------------------------------------------------------------------------------
# GC
#-------------------------------------------------------------------------------

def runGc(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.read() #reads in files


    # A Python program to print all
    # permutations using library function
    from itertools import permutations

    # Get all permutations of [1, 2, 3]
    perm = permutations([1, 2, 3])

    # Print the obtained permutations
    for i in list(perm):
        print i



#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
