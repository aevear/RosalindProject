#-------------------------------------------------------------------------------
# Fibd
#-------------------------------------------------------------------------------
def runFibd(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.readline().split() #reads in files
    n, m = int(inputData[0]), int(inputData[1])
    sequence = list()
    
    for i in range(n):
        if i < 2:
            # Normal Fibonacci initialization
            total = 1
            sequence.append(total)
        elif (i < m) or (m == 0):
            # Normal Fibonacci calculation
            total = sequence[i - 1] + sequence[i - 2]
            sequence.append(total)
        elif i == m:
            # Now we need R(n - (m + 1)), but i - (m + 1) < 0, so we have to
            # provide the missing value
            total = sequence[i - 1] + sequence[i - 2] - 1
            sequence.append(total)
        else:
            # i - (m + 1) >= 0, so we can get the value from the sequence
            total = sequence[i - 1] + sequence[i - 2] - sequence[i - (m + 1)]
            sequence.append(total)
    return total

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
