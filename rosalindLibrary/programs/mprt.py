#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from urllib import urlopen
#-------------------------------------------------------------------------------
# Mprt
#-------------------------------------------------------------------------------
def runMprt(inputFile):
    fi = open(inputFile, 'r') #reads in the file that list the before/after file names
    inputData = fi.read().split("\n") #reads in files
    inputData = inputData[:-1]
    dataPackages, results = [], []

    #this part imports the information from online
    for k in inputData:
        dataPackages.append(urlopen("http://www.uniprot.org/uniprot/" + k + ".fasta"))

    #Compile the lines and removes the initial line. Will be useful in the next bit
    compiledLine, compiledLines = '', []
    for k in dataPackages:
        compiledLine = ''
        for line in k:
            if line[0] != ">":
                compiledLine = compiledLine + line.strip("\n")
        compiledLines.append(compiledLine)


    #This part actually looks for the motif and complies to something useful to report
    inputCounter = 0
    for line in compiledLines:
        hasMotif = False
        motifLocations = list()
        for index in range(len(line)-3):
            if line[index] == "N":
                if (line[index + 1] != "P") and ((line[index +2] == "S") or (line[index +2] == "T")) and (line[index +3] != "P"):
                    hasMotif = True
                    motifLocations.append(str(index + 1))
        if hasMotif == True:
            results.append(str(inputData[inputCounter] + "\n" + " ".join(motifLocations) + "\n")) #combines the string into a reportable format
        inputCounter += 1



    return "".join(results)
    #return compiledLines

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
