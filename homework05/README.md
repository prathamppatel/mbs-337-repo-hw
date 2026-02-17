# Homework 05

This directory contains a Python script for summarizing residue information from a protein structure file.

## Exercise: mmCIF Chain Summary

**Script:** `mmcif_summary.py`  
**Input:** `4HHB.cif`  

This script reads a mmCIF file using `MMCIFParser` from Biopython.  
It looks at the first model in the structure and summarizes each chain.

For each chain, the script calculates:

- Chain ID  
- Total number of residues  
- Number of standard (non-hetero) residues  
- Number of hetero residues  

The results are written to a JSON file in the required format.

## Running the Script

The script is run from the terminal using Python.  
A logging level can be set using the `-l` flag (DEBUG, INFO, WARNING, or ERROR).

## Input File

The input file is the hemoglobin structure `4HHB.cif`, which can be downloaded from the RCSB Protein Data Bank.

## Output Files

This script creates a summary file located in the `output_files` folder:

- `4HHB_summary.json`

This file contains the per-chain residue counts for the structure.
