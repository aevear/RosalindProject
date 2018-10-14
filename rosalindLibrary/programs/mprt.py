#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from urllib import urlopen

#r = urlopen("http://download.cathdb.info/cath/releases/all-releases/v4_2_0/cath-classification-data/cath-domain-list-v4_2_0.txt")

#-------------------------------------------------------------------------------
# Mprt
#-------------------------------------------------------------------------------

def runMprt(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.read().split("\n") #reads in files
    inputData = inputData[:-1]
    dataPackages = []

    for k in inputData:
        dataPackages.append(urlopen("http://www.uniprot.org/uniprot/" + k + ".fasta"))

    #N{P}[ST]{P}

    #Compile the lines
    counter = 0
    compiledLine, compiledLines = '', []
    for k in dataPackages:
        for line in k:
            if line[0] != ">":
                compiledLine = compiledLine + line[:-1]
        compiledLines.append(compiledLine)


    return compiledLines

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
