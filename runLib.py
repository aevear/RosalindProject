#-------------------------------------------------------------------------------
# DNA
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Basic Libraries
#-------------------------------------------------------------------------------
import sys
import os
#-------------------------------------------------------------------------------
# Written Libraries
#-------------------------------------------------------------------------------
from rosalindLibrary.programs.dna import runDna
from rosalindLibrary.programs.rna import runRna
from rosalindLibrary.programs.revc import runRevc
from rosalindLibrary.programs.iprb import runIprb
from rosalindLibrary.programs.fib import runFib
from rosalindLibrary.programs.gc import runGc
from rosalindLibrary.programs.prot import runProt
from rosalindLibrary.programs.subs import runSubs

#-------------------------------------------------------------------------------
# Code
#-------------------------------------------------------------------------------
#print a list of commands
commands = {
    "dna" : runDna,
    "rna" : runRna,
    "revc" : runRevc,
    "iprb" : runIprb,
    "fib" : runFib,
    "gc" : runGc,
    "prot" : runProt,
    "subs" : runSubs
}

chosenProgram = sys.argv[1]

if chosenProgram in commands:
    direct = os.getcwd()
    x_file = direct+"/inputs/rosalind_"+chosenProgram+".txt"
    func = commands[chosenProgram]
    print(func(x_file))

    # You could also shorten this to:
    # commands[user_input]()
else:
    print("Command not found.")


















#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------
