#-------------------------------------------------------------------------------
# Lgis
#-------------------------------------------------------------------------------
global maximum
global minimum

def dynamicLoop(arr , n ):
    # to allow the access of global variable
    global maximum

    # Base Case
    if n == 1 :
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in xrange(1, n):
        res = dynamicLoop(arr , i)
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
    dynamicLoop(permArray, len(permArray))

    return maximum


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
