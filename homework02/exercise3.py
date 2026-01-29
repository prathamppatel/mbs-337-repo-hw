
def base_percentages(bio_sequence):
    A_count = 0
    C_count = 0
    T_count = 0
    G_count = 0

    for nucleotide in bio_sequence:
        if nucleotide == 'A':
            A_count = A_count + 1
        elif nucleotide == 'T':
            T_count = T_count + 1
        elif nucleotide == 'C':
            C_count = C_count + 1
        elif nucleotide == 'G':
            G_count = G_count + 1
    
    percents = {
        'A': round(A_count/len(bio_sequence), 2),
        'T': round(T_count/len(bio_sequence), 2),
        'C': round(C_count/len(bio_sequence), 2),
        'G': round(G_count/len(bio_sequence), 2)
    }

    return(percents)

final = base_percentages("ATCGATCGGGCATA")
print(final)