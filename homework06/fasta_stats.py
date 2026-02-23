#!/usr/bin/env python3
from Bio.SeqIO.FastaIO import SimpleFastaParser
import argparse
import logging
import socket
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--loglevel',
                    type=str,
                    required=False,
                    default='WARNING',
                    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL')
parser.add_argument('-i', '--input',
                    type=str,
                    required=False,
                    default='immune_proteins.fasta',
                    help='Input FASTA file')
parser.add_argument('-o', '--output',
                    type=str,
                    required=False,
                    default='immune_proteins_stats.txt',
                    help='Output stats text file')
args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)

def fasta_stats(filename: str, output_file: str) -> None:
    """
    Reads a FASTA file and writes sequence statistics to a text file.

    Args:
        filename (str): Path to the FASTA file.
        output_file (str): Path to the output text file where stats will be written.
    Returns:
        None
    """
    seq_num = 0
    total_residues = 0
    longest_sequence = 0
    longest_accession = None
    shortest_sequence = 100000000000000
    shortest_accession = None
    try:
        logging.info(f"Reading FASTA file {filename}")
        with open(filename, 'r') as f:
            for header, sequence in SimpleFastaParser(f):
                seq_num += 1
                total_residues += len(sequence)
                parts = header.split('|')

                if len(sequence) > longest_sequence:
                    longest_sequence = len(sequence)
                    longest_accession = parts[1]

                if len(sequence) < shortest_sequence:
                    shortest_sequence = len(sequence)
                    shortest_accession = parts[1]
        with open(output_file, 'w') as out:
            out.write(f"Num Sequences: {seq_num}\n")
            out.write(f"Total Residues: {total_residues}\n")
            out.write(f"Longest Accession: {longest_accession} ({longest_sequence} residues)\n")
            out.write(f"Shortest Accession: {shortest_accession} ({shortest_sequence} residues)\n")

    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error reading FASTA file: {e}")
        sys.exit(1)
    
def main():
    fasta_stats(args.input, args.output)

if __name__ == "__main__":
    main()