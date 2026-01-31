import json
from pydantic import BaseModel
with open('hw_input.json', 'r') as f:
    bio_data = json.load(f)

class ProteinEntry(BaseModel):
    primaryAccession: str
    organism: dict
    proteinName: str
    sequence: dict
    geneName: str
    function: str


#first_protein_dict = bio_data["protein_list"][0]
#protein = ProteinEntry(**first_protein_dict)
#print(protein)

proteins = []
for data in bio_data["protein_list"]:
    proteins.append(ProteinEntry(**data))

#for protein in proteins:
#    print(protein.primaryAccession)

#print(proteins[0].sequence["mass"])


def find_total_mass():
    total_mass: int = 0
    for protein in proteins:
        total_mass += protein.sequence["mass"]
    print(total_mass)


find_total_mass()

def find_large_proteins():
    large_proteins: list[str] = []
    for protein in proteins:
        if protein.sequence["length"] >= 1000:
            large_proteins.append(protein.proteinName)
    print(large_proteins)

find_large_proteins()

def find_non_eukaryotes():
    non_eukaryotes: list[str] = []
    for protein in proteins:
        if "Eukaryota" not in protein.organism["lineage"]:
            non_eukaryotes.append(protein.proteinName)
    print(non_eukaryotes)

find_non_eukaryotes()