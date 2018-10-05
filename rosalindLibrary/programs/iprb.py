#-------------------------------------------------------------------------------
# Revc
#-------------------------------------------------------------------------------

def runIprb(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    activityFile = fi.readline().split() #reads in files
    k, m, n = float(activityFile[0]), float(activityFile[1]), float(activityFile[2])

    total = k + m + n

    r_r = (n / total) * ((n - 1) / (total - 1))
    d_d = (m / total) * ((m - 1) / (total - 1))
    d_r = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))

    k_total = r_r + d_d * 1/4 + d_r * 1/2
    k_total =  1 - k_total

    return str(k_total)


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
