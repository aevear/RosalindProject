#-------------------------------------------------------------------------------
# Import Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.loaders.rosalindLoader import rosalindLoader
#-------------------------------------------------------------------------------
# Tran
#-------------------------------------------------------------------------------
transitionTable = [ ('A', 'G'),
                    ('G', 'A'),
                    ('C', 'T'),
                    ('T', 'C') ]

transversionTable = [ ('A', 'C'),
                      ('C', 'A'),
                      ('G', 'T'),
                      ('T', 'G'),
                      ('A', 'T'),
                      ('T', 'A'),
                      ('C', 'G'),
                      ('G', 'C') ]

def runTran(inputFile):
    fastaNames, fastaData = rosalindLoader(inputFile)
    transition, transversion = 0.0, 0.0

    for k in zip(fastaData[0], fastaData[1]):
        if k in transitionTable:
            transition += 1.0
        if k in transversionTable:
            transversion += 1.0
    return transition/transversion


#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
