#-------------------------------------------------------------------------------
# Lgis
#-------------------------------------------------------------------------------
global maximum
global minimum

def dynamicLoopHigh(arr , n ):
    # to allow the access of global variable
    global maximum

    # Base Case
    if n == 1 :
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    for i in xrange(1, n):
        res = dynamicLoopHigh(arr , i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res +1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum , maxEndingHere)

    return maxEndingHere


def runLgis(inputFile):
    fi = open(inputFile, 'r')
    inputData, permArray = fi.readline(), fi.readline().strip("\n").split(" ")
    highestPath, lowestPath = [], []
    global maximum
    maximum = 1
    dynamicLoopHigh(permArray, len(permArray))

    return maximum


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
