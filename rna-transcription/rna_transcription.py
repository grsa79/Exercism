DNA = ["G", "C","T", "A"]
RNA = ["C", "G","A", "U"]


def to_rna(dna_strand:str) -> str:
    """
    determines RNA complement to given DNA
    :dna_strand - str containing given DNA
    :returns str - RNA complement
    """
    rna_strand = ""
    for acid in dna_strand:
        if not acid in DNA: raise ValueError("invalid DNA strand given")
        rna_strand += RNA[DNA.index(acid)]
    return rna_strand
