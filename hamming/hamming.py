
def distance(dna_strand_one, dna_strand_two):
    # Check if both have same size
    if len(dna_strand_one) != len(dna_strand_two):
        raise ValueError

    distance_count = 0

    for nucleotide_one, nucleotide_two in zip(dna_strand_one, dna_strand_two):
        if not nucleotide_one == nucleotide_two:
            distance_count += 1

    return distance_count

