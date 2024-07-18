def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    count_sequence = 0
    
    for n in dna:
        count_sequence = count_sequence + 1 

    return count_sequence

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count_nucleotide = 0
    for n in dna:
        if n == nucleotide:
            count_nucleotide = count_nucleotide + 1

    return count_nucleotide
            
def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs
    in the DNA sequence dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return (dna2 in dna1)

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if DNA sequence dna1 is valid, that is
    it contains only characters, 'A', 'T', 'C', 'G'
    
    >>> is_valid_sequence('atcg')
    Fasle
    >>> is_valid_sequence('ATC')
    True
    >>> is_valid_sequence('ATCH')
    False
    
    '''
    
    if dna.islower():
        return False
    
    valid_nucleotides = 'ATCG'
    for n in dna:
        if n not in valid_nucleotides:
            return False

    return True

def insert_sequence(dna1, dna2, i):
    ''' (str, str, int) -> str

    Return the DAN sequence obtained by inserting the seconds DNA dna2 into
    the first DAN sequence dna1 at the given index i.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('CCGG', 'AT', 0)
    ATCCGG
    >>> insert_sequence('CCGG' , 'AT', len('CCGG')-1)
    CCGATG
    >>> insert_sequence('CCGG', 'AT', -2)
    CCATGG
    >>> insert_sequence('CCGG', 'AT', -1)
    CCGATG

    '''
    
    return dna1[:i] + dna2 + dna1[i:]
    

def get_complement(nucleotide):
    ''' (str)-> str

    Return the nucleotide's complement

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C

    '''

    n_complement =''
    if nucleotide in 'A':
        n_complement = 'T'
    elif nucleotide in 'T':
        n_complement = 'A'
    elif nucleotide in 'C':
        n_complement = 'G'
    else:
        n_complement = 'C'

    return n_complement

def get_complementary_sequence(dna):
    ''' (str) -> str

    Return the complementary sequence of the DNA dna
    
    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('GC')
    CG
    
    '''
    
    dna_complement = ''
    for n in dna:
        dna_complement = dna_complement + get_complement(n)

    return dna_complement
