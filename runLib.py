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
from rosalindLibrary.programs.prob import runProb
from rosalindLibrary.programs.sseq import runSseq
from rosalindLibrary.programs.lexf import runLexf
from rosalindLibrary.programs.hamm import runHamm
from rosalindLibrary.programs.iev import runIev

#-------------------------------------------------------------------------------
# Code
#-------------------------------------------------------------------------------
#print a list of commands
sys.dont_write_bytecode = True
commands = {
    "dna" : runDna,
    "rna" : runRna,
    "revc" : runRevc,
    "iprb" : runIprb,
    "fib" : runFib,
    "gc" : runGc,
    "prot" : runProt,
    "subs" : runSubs,
    "prob" : runProb,
    "sseq" : runSseq,
    "lexf" : runLexf,
    "hamm" : runHamm,
    "iev" : runIev

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
