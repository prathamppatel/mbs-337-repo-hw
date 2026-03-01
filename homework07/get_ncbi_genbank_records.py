#!/usr/bin/env python3
from Bio import Entrez, SeqIO
import argparse
import logging
import socket
import redis
import json
import sys

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

def get_records() -> tuple[list, list]:
    """
    Searches the NCBI Protein database and fetches full GenBank records.
    
    Args:
        None.
        
    Returns:
        records: A list of BioPython SeqRecord objects.
        id_list: A list of strings representing the NCBI GI numbers.
    """

    Entrez.email = "your_email@example.com" 
    
    try:
        logging.info("Searching NCBI Protein database for Arabidopsis thaliana AT5G10140.")       
        with Entrez.esearch(db="protein", term="Arabidopsis thaliana AND AT5G10140", retmax=30) as h:
            results = Entrez.read(h)
            id_list = results.get("IdList", [])
    
    except:
        logging.error("No records found.")
        sys.exit(1)

    logging.info(f"Fetching {len(id_list)} records...")
    records = []
    with Entrez.efetch(db="protein", id=",".join(id_list), rettype="gb", retmode="text") as h:
        records = list(SeqIO.parse(h, "gb"))
            
    return records, id_list

def store_and_write_records(id_list: list, records: list, output_file: str) -> None: 
    """
    Stores record data in a Redis database and writes formatted data to a text file.
    
    Args:
        id_list: A list of strings (GIs) to be used as Redis keys.
        records: A list of SeqRecord objects containing protein data.
        output_file: A string representing the name of the file to be created.
        
    Returns:
        None.
    """
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    logging.info("Connecting to Redis to store records.")
    for i in range(len(id_list)):
        gi_id = id_list[i]
        rec = records[i]
        
        record_dict = {
            "ID": rec.id,
            "Name": rec.name,
            "Description": rec.description,
            "Sequence": str(rec.seq)
        }
        r.set(gi_id, json.dumps(record_dict))

    with open(output_file, "w") as f:
        for gi_id in id_list:
            data = json.loads(r.get(gi_id))
            f.write(f"ID: {data['ID']}\n")
            f.write(f"Name: {data['Name']}\n")
            f.write(f"Description: {data['Description']}\n")
            f.write(f"Sequence: {data['Sequence']}\n\n")


def main():
    output_file = "genbank_records.txt"
    records, id_list = get_records()
    store_and_write_records(id_list, records, output_file)

if __name__ == "__main__":
    main()