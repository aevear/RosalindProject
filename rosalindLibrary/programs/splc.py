#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
from rosalindLibrary.tools.rosalindTools import nucToProtien
#-------------------------------------------------------------------------------
# Splc
#-------------------------------------------------------------------------------
def runSplc(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    splicedDNA, looping, readingFrame, protienString = fastaData[0], True, 0, ""

    #Need to splice out the introns, and this is a simple way of doing it
    for k in fastaData[1:]:
        splicedDNA = splicedDNA.replace(k,"")

    #Now we need to begin translating the string, maybe we could use other program?
    while looping:
        if (len(splicedDNA) - readingFrame ) < 3:
            looping = False
        else:
            newProtien = nucToProtien(splicedDNA[readingFrame:readingFrame+3])
            if newProtien == "Stop":
                looping = False
                return protienString
            else:
                protienString = protienString + newProtien
                #print protienString
                readingFrame +=3

    return splicedDNA

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
