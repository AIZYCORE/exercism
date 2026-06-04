"""A Python function for the RNA complementary sequence of a given DNA sequence."""

def to_rna(dna_strand):
    """determine the RNA complement of a given DNA sequence.
    
    :param dna_strand: str - DNA sequence.
    :return: str - Corresponding complementary RNA sequence.
    """
    rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join([rna[i] for i in dna_strand])
    
    
        