# Homework 05

This repository contains Python scripts for processing biological sequence and structure data.  
All scripts are container-ready and can be run inside a Docker container.

## Scripts Overview

### 1. `fasta_stats.py`

**Input:** FASTA file (default: `immune_proteins.fasta`)  
**Output:** Text file with sequence statistics (default: `immune_proteins_stats.txt`)  

This script reads a FASTA file and calculates:

- Number of sequences  
- Total residues  
- Longest sequence (accession and length)  
- Shortest sequence (accession and length)  

### 2. `fasta_filter.py`

**Input:** FASTA file (default: `immune_proteins.fasta`)  
**Output:** Filtered FASTA file (default: `long_only.fasta`)  
**Optional Parameter:** Minimum sequence length (`-m`, default: 1000)  

This script filters sequences from the input FASTA file, keeping only those equal to or longer than the minimum length.

### 3. `fastq_filter.py`

**Input:** FASTQ file (default: `sample1_rawReads.fastq`)  
**Output:** Filtered FASTQ file (default: `sample1_cleanReads.fastq`)  
**Optional Parameters:**  
- FASTQ encoding (`-e`, default: `fastq-sanger`)  
- Minimum average Phred quality (`-p`, default: 30)  

This script filters reads based on average Phred quality scores.

### 4. `mmcif_summary.py`

**Input:** mmCIF file (default: `4HHB.cif`)  
**Output:** JSON file (default: `4HHB_summary.json`)  

This script summarizes per-chain residue information from a protein structure:

- Chain ID  
- Total residues  
- Standard residues  
- Hetero residues  

---

## Running the Scripts in Docker

### 1. Build the Docker Image

After cloning the repository, navigate into the project directory (the directory containing the Dockerfile).

Build the Docker image using:

'docker build -t homework06:1.0 .'

### 2. Download the Input Data

**The following input files are required:** immune_proteins.fasta, sample1_rawReads.fastq, 4HHB.cif

The mmCIF structure file (4HHB.cif) was obtained from the RCSB Protein Data Bank:

4HHB — Human Hemoglobin
Source: https://www.rcsb.org/structure/4HHB

Place all input files inside the project directory.
Create an output directory:

'mkdir -p output_files'

### 3. Mount the Project Directory Into the Container

When running the container, the current working directory must be mounted into the container using the -v flag.
This mounts your local project directory to /data inside the container.

### 4. Run the Container as Your User

To prevent output files from being owned by root, run the container using your user ID and group ID:

'-u $(id -u):$(id -g)'

### 5. Running Each Script

All scripts are located inside the container at /code/.

A. FASTA Filter

Filters sequences from a FASTA file.

Parameters:

- i : input FASTA file

- o : output FASTA file

code:

'docker run --rm -u $(id -u):$(id -g) -v $PWD:/data homework06:1.0 \
python /code/fasta_filter.py \
-i /data/immune_proteins.fasta \
-o /data/output_files/fasta_filtered.fasta'

Output:

- output_files/fasta_filtered.fasta

### B. FASTA Statistics

Computes statistics for a FASTA file.

Parameters:

-i : input FASTA file

-o : output text file

code:

'docker run --rm -u $(id -u):$(id -g) -v $PWD:/data homework06:1.0 \
python /code/fasta_stats.py \
-i /data/output_files/fasta_filtered.fasta \
-o /data/output_files/fasta_stats.txt'

Output:

- output_files/fasta_stats.txt

### C. FASTQ Filter

Filters reads from a FASTQ file.

Parameters:

- i : input FASTQ file

- o : output FASTQ file

code:

'docker run --rm -u $(id -u):$(id -g) -v $PWD:/data homework06:1.0 \
python /code/fastq_filter.py \
-i /data/sample1_rawReads.fastq \
-o /data/output_files/sample1_filtered.fastq'

Output:

- output_files/sample1_filtered.fastq

### D. mmCIF Summary

Parses an mmCIF structure file and outputs per-chain residue statistics in JSON format.

Parameters:

- i : input mmCIF file

- o : output JSON file

code:

'docker run --rm -u $(id -u):$(id -g) -v $PWD:/data homework06:1.0 \
python /code/mmcif_summary.py \
-i /data/4HHB.cif \
-o /data/output_files/mmcif_summary.json'

Output:

- output_files/mmcif_summary.json


## Access Docker Image:

To access Docker Image:


code: 

'docker pull prathamppatel/homework06:1.0'




