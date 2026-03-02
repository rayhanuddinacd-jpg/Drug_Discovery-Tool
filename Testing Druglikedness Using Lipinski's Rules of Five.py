from rdkit import Chem 
from rdkit.Chem import Descriptors 
 
def analyze_drug_likeness(smiles): 
    molecule = Chem.MolFromSmiles(smiles) 
    if molecule: 
        mw = Descriptors.MolWt(molecule) 
        logp = Descriptors.MolLogP(molecule) 
        h_donors = Descriptors.NumHDonors(molecule) 
        h_acceptors = Descriptors.NumHAcceptors(molecule) 
  
        violations = 0 
        if mw > 500:  # Molecular Weight > 500 
            violations += 1 
        if logp > 5:  # LogP > 5 
            violations += 1 
        if h_donors > 5:  # H-Donors > 5 
            violations += 1 
        if h_acceptors > 10:  # H-Acceptors > 10 
            violations += 1 
 
        return { 
            "SMILES": smiles, 
            "Molecular Weight": mw, 
            "LogP": logp, 
            "H-Donors": h_donors, 
            "H-Acceptors": h_acceptors, 
            "Violations": violations 
        } 
    else: 
        return {"SMILES": smiles, "Error": "Invalid SMILES"} 
 
smiles_list = []
results = [] 
for smiles in smiles_list: 
    result = analyze_drug_likeness(smiles) 
    results.append(result) 
 
for res in results: 
    print(res) 
import csv 

with open("drug_likeness_results_with_violations.csv", mode="w", 
newline="") as file: 
    writer = csv.DictWriter(file, fieldnames=["SMILES", "Molecular Weight", 
"LogP", "H-Donors", "H-Acceptors", "Violations", "Error"]) 
    writer.writeheader() 
    writer.writerows(results) 
print("done")