import os 
print(os.getcwd()) 
import pubchempy as pcp 
 
def fetch_smiles_and_name(cids): 
    result = [] 
    for cid in cids: 
        compound = pcp.Compound.from_cid(cid) 
        if compound: 
            smiles = compound.canonical_smiles 
            result.append(f"{smiles}") 
    return result 
cid_list = []
output = fetch_smiles_and_name(cid_list) 
for line in output: 
    print(line) 
with open(r"C:\Users\HP\Desktop\smiles.txt", "w") as file: 
    for line in output: 
        file.write(line + "\n") 
print("saved to smiles_with_raian.txt")