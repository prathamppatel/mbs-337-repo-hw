# Homework 04

This directory contains Python scripts for working with biological sequence and structure data.

## Exercise 1: Count residues in FASTA file

**Script:** `exercise1.py`  
**Input:** `immune_proteins.fasta`  

This script reads a FASTA file and prints:

- Total number of sequences  
- Total number of residues  
- Accession ID and length of the longest sequence  
- Accession ID and length of the shortest sequence 

## Exercise 2: Write new FASTA file

**Script:** `exercise2.py`  
**Input:** `immune_proteins.fasta`  

This script writes a new FASTA file called `long_only.fasta` containing only sequences longer than or equal to 1000 residues. The headers from the original FASTA are preserved. The output contains 33 sequences.

## Exercise 3: FASTQ quality filter and write

**Script:** `exercise3.py`  
**Input:** `sample1_rawReads.fastq`  

This script reads a FASTQ file, keeps only reads with average Phred quality ≥ 30, and writes them to `sample1_cleanReads.fastq`. It also prints:

- Total reads in the original file  
- Number of reads passing quality control

## Exercise 4: mmCIF multi-chain summary

**Script:** `exercise4.py`  
**Input:** `4HHB.cif`  

This script parses a multi-chain mmCIF file using `MMCIFParser`. For each chain, it prints:

- Chain ID  
- Number of non-hetero residues  
- Number of atoms in those residues

## Input Files

- `immune_proteins.fasta` for Exercises 1 and 2  
- `sample1_rawReads.fastq` for Exercise 3  
- `4HHB.cif` for Exercise 4  

## Output Files

All generated files are in `output_files/`:

- `long_only.fasta` (Exercise 2)  
- `sample1_cleanReads.fastq` (Exercise 3)