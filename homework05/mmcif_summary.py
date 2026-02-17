import json
import argparse
import logging
import socket
import sys
from Bio.PDB.MMCIFParser import MMCIFParser

# Constants
MMCIF_FILE = '4HHB.cif'
OUTPUT_JSON = '4HHB_summary.json'

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--loglevel',
                    type=str,
                    required=False,
                    default='WARNING',
                    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL')
args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)

def parse_mmcif_file(mmcif_file: str) -> object: 
    """
    Reads an mmCIF file and returns the parsed structure.

    Args:
        mmcif_file (str): Path to the mmCIF file.

    Returns:
        Structure object from MMCIFParser if successful.
    """
    parser = MMCIFParser()
    try:
        structure = parser.get_structure('DHB', mmcif_file)
        logging.debug(f"{mmcif_file} has been parsed through correctly.")
        return structure
    except FileNotFoundError:
        logging.error(f"Input MMCIF file {mmcif_file} not found.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error parsing '{mmcif_file}': {e}.")
        sys.exit(1)

def summarize_structure(structure: object) -> list:
    """
    Summarizes the chains of the first model in a parsed mmCIF structure.
    Finds and returns a list of the chain id, total number of residues,
    number of standard residues, and number of hetero residues. 

    Args:
        structure: Parsed structure object from MMCIFParser.

    Returns:
        summary: a list of dictionaries with each chain's ID, total residues, 
        standard residues, and hetero residue count.
    """
    logging.info(f"Reading parsed MMCIF file {MMCIF_FILE}.")
    summary = []
    # Setting the first model in structure as the model
    model = structure[0]
    for chain in model:
        residue_num = 0
        standard_num = 0
        het_res_num = 0
        for residue in chain:
            residue_num += 1
            if residue.get_id()[0] == ' ':
                standard_num += 1
            else:
                het_res_num += 1
        summary.append({
            "chain_id": chain.get_id(),
            "total_residues": residue_num,
            "standard_residues": standard_num,
            "hetero_residue_count": het_res_num
        })
    logging.info(f"Finished reading parsed MMCIF file {MMCIF_FILE}. {len(summary)} chains processed.")
    return summary

def write_json_out(summary: list, output_json: str) -> None:
    """
    Writes the summary of chains to a JSON file.

    Args:
        summary: List of dictionaries with chain information.
        output_json: Path to the JSON file to write the output.

    Returns:
        None
    """
    logging.info(f"Writing summary to {output_json}.")
    output = {"chains": summary}
    with open(output_json, 'w') as f:
        json.dump(output, f, indent=2)
    logging.info(f"Finished writing {output_json}.")

def main():
    logging.info("Starting MMCIF summary workflow.")
    structure = parse_mmcif_file(MMCIF_FILE)
    summary = summarize_structure(structure)
    write_json_out(summary, OUTPUT_JSON)
    logging.info("MMCIF summary workflow complete.")

if __name__ == "__main__":
    main()
