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
                    default='long_only.fasta',
                    help='Output FASTA file')
parser.add_argument('-m', '--min_length',
                    type=int,
                    required=False,
                    default=1000,
                    help='Minimum sequence length to keep')

args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)


def fasta_filter(input_file: str, output_fasta: str, min_length: int) -> None:
    """
    Reads a FASTA file and writes sequences >= 1000 residues to a new FASTA file.

    Args:
        input_file (str): Path to the input FASTA file.
        output_fasta (str): Path to the output FASTA file.
        min_length (int): Minimum sequence length to keep.


    Returns:
        None
    """
    try:
        with open(input_file, 'r') as infile, open(output_fasta, 'w') as outfile:
            for header, sequence in SimpleFastaParser(infile):
                if len(sequence) >= min_length:
                    outfile.write(f">{header}\n")
                    outfile.write(f"{sequence}\n")
    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error processing FASTA file: {e}")
        sys.exit(1)

def main():
    fasta_filter(args.input, args.output, args.min_length)

if __name__ == "__main__":
    main()

