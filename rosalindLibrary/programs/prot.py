#-------------------------------------------------------------------------------
# Prot
#-------------------------------------------------------------------------------

def runProt(inputFile):
    fi = open(inputFile, "r")
    dnaSequence = fi.read().strip()

    codonDic = {'UUU' : 'F', 'CUU' :  'L', 'AUU' : 'I', 'GUU' : 'V', 'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V', 'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V', 'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V', 'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A', 'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A', 'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A', 'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A', 'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D', 'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D', 'UAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'UAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E', 'UGU' : 'C', 'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G', 'UGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G', 'UGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G', 'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'}

    protein, counter = "", 0

    for i in dnaSequence[:len(dnaSequence)-2]:
        if counter % 3 == 0:
            if (codonDic[i + dnaSequence[counter + 1] + dnaSequence[counter + 2]]) == "Stop":
                break
            protein = protein + (codonDic[i + dnaSequence[counter + 1] + dnaSequence[counter + 2]])
        counter += 1

    return protein

#-------------------------------------------------------------------------------
# Fin
#-------------------------------------------------------------------------------




























#
