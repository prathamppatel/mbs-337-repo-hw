from Bio import SeqIO

num_reads = 0
num_kept = 0
with open('sample1_rawReads.fastq', 'r') as infile, open('sample1_cleanReads.fastq', 'w') as outfile:
    for record in SeqIO.parse(infile, 'fastq-sanger'):
        num_reads += 1
        avg_phred_qual = sum(record.letter_annotations['phred_quality'])/len(record.letter_annotations['phred_quality'])
        if avg_phred_qual >= 30:
            SeqIO.write(record, outfile, 'fastq-sanger')
            num_kept +=1
            

print(f"Total reads in original file: {num_reads}")
print(f"Reads passing filter: {num_kept}")