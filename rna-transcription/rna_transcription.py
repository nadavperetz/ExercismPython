rna_transcription_dict = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    rna_strand = ""
    for nucleotide in dna_strand:
        try:
            rna_strand += rna_transcription_dict[nucleotide]
        except KeyError:
            return ''
    return rna_strand

