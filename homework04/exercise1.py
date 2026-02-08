from Bio.SeqIO.FastaIO import SimpleFastaParser

seq_num = 0
total_residues = 0
longest_sequence = 0
longest_accession = None
shortest_sequence = 1000000000000000
shortest_accession = None
with open('immune_proteins.fasta', 'r') as f:
    for header, sequence in SimpleFastaParser(f):
        seq_num += 1 
        total_residues += len(sequence)
       #print(f"header: {header}")
        parts = header.split('|')
        if len(sequence) > longest_sequence:
            longest_sequence = len(sequence)
            longest_accession = parts[1]
        if len(sequence) < shortest_sequence:
            shortest_sequence = len(sequence)
            shortest_accession = parts[1]
         
        
        
print(f"Num Sequences: {seq_num}")
print(f"Total Residues: {total_residues}")
print(f"Longest Accession: {longest_accession} ({longest_sequence} residues)")
print(f"Shortest Accession: {shortest_accession} ({shortest_sequence} residues)")