#!/usr/bin/env python3
from Bio import SeqIO
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
                    default='sample1_rawReads.fastq',
                    help='Input FASTQ file')
parser.add_argument('-o', '--output',
                    type=str,
                    required=False,
                    default='sample1_cleanReads.fastq',
                    help='Output FASTQ file')
parser.add_argument('-e', '--encoding',
                    type=str,
                    required=False,
                    default='fastq-sanger',
                    help='FASTQ encoding (fastq-sanger, fastq-illumina, etc.)')
parser.add_argument('-p', '--phred',
                    type=int,
                    required=False,
                    default=30,
                    help='Minimum average Phred quality score to keep a read')
args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)

def fastq_filter(infile: str, outfile: str, encoding: str, min_phred: int) -> None:
    """
    Reads a FASTQ file and writes reads with average Phred quality >= min_phred
    to a new FASTQ file.

    Args:
        infile (str): Path to the input FASTQ file.
        outfile (str): Path to the output FASTQ file.
        encoding (str): FASTQ encoding (fastq-sanger, fastq-illumina, etc.).
        min_phred (int): Minimum average Phred quality score to keep a read.

    Returns:
        None
    """
    num_reads = 0
    num_kept = 0

    try:
        logging.info(f'Reading FASTQ file {infile}')
        with open(infile, 'r') as in_f, open(outfile, 'w') as out_f:
            for record in SeqIO.parse(in_f, encoding):
                num_reads += 1
                avg_phred_qual = sum(record.letter_annotations['phred_quality']) / len(record.letter_annotations['phred_quality'])
                if avg_phred_qual >= min_phred:
                    SeqIO.write(record, out_f, encoding)
                    num_kept += 1

        logging.info(f"Total reads in original file: {num_reads}")
        logging.info(f"Reads passing filter: {num_kept}")

    except FileNotFoundError:
        logging.error(f"File not found: {infile}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error processing FASTQ file: {e}")
        sys.exit(1)


def main():
    fastq_filter(args.input, args.output, args.encoding, args.phred)

if __name__ == "__main__":
    main()

