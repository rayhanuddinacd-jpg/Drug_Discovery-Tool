This repository contains Python scripts for basic computational drug discovery workflows, including:
Downloading SDF files from PubChem using CID
Retrieving SMILES from PubChem using CID
Testing drug-likeness using Lipinski’s Rule of Five
These tools demonstrate basic in-silico screening and molecular data handling.

Files Description:
1. download_sdf_from_cid.py
Downloads molecular structure files (SDF format) from PubChem using Compound ID (CID).
2. retrieve_smiles_from_cid.py
Retrieves SMILES string of a compound from PubChem using CID.
3. lipinski_druglikeness.py
Evaluates drug-likeness based on Lipinski's Rule of Five:
Molecular weight < 500
LogP < 5
Hydrogen bond donors ≤ 5
Hydrogen bond acceptors ≤ 10

Technologies Used

Python
Requests library
RDKit
PubChem

How to Run:
Install required libraries:

Run script:

Purpose
This project was developed as part of self-learning in computational drug discovery and cheminformatics.
