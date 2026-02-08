from Bio.PDB.MMCIFParser import MMCIFParser

parser = MMCIFParser()

with open('4HHB.cif', 'r') as f:
    structure = parser.get_structure('DHB', f)
    for model in structure:
        for chain in model:
            residue_num = 0
            atom_num = 0
            for residue in chain:
              if residue.get_id()[0] == ' ':
                residue_num += 1
                for atom in residue:
                    atom_num += 1
            print(f"Chain {chain.get_id()}: {residue_num} residues, {atom_num} atoms")