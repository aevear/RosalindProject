#-------------------------------------------------------------------------------
# Rosalind Tools
#-------------------------------------------------------------------------------
def DnaCombinationTable(aminoAcid):
    DnaCombinationTable = {
    'F' : 2,
    'L' : 6,
    'S' : 6,
    'Y' : 2,
    'C' : 2,
    'W' : 1,
    'P' : 4,
    'H' : 2,
    'Q' : 2,
    'R' : 6,
    'I' : 3,
    'M' : 1,
    'T' : 4,
    'N' : 2,
    'K' : 2,
    'V' : 4,
    'A' : 4,
    'D' : 2,
    'E' : 2,
    'G' : 4,
    }

    return DnaCombinationTable[aminoAcid]




def monoisotopicTable(isotope):
    monoisoTable = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333,
    }

    return monoisoTable[isotope]

def nucToProtien(codon):
    codonDic = {'TTT' : 'F', 'CTT' :  'L', 'ATT' : 'I', 'GTT' : 'V', 'TTC' : 'F', 'CTC' : 'L', 'ATC' : 'I', 'GTC' : 'V', 'TTA' : 'L', 'CTA' : 'L', 'ATA' : 'I', 'GTA' : 'V', 'TTG' : 'L', 'CTG' : 'L', 'ATG' : 'M', 'GTG' : 'V', 'TCT' : 'S', 'CCT' : 'P', 'ACT' : 'T', 'GCT' : 'A', 'TCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A', 'TCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A', 'TCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A', 'TAT' : 'Y', 'CAT' : 'H', 'AAT' : 'N', 'GAT' : 'D', 'TAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D', 'TAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'TAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E', 'TGT' : 'C', 'CGT' : 'R', 'AGT' : 'S', 'GGT' : 'G', 'TGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G', 'TGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G', 'TGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'}

    return codonDic[codon]

#
