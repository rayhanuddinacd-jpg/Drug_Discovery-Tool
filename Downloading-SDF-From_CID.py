import requests 
 
cid_list=[]
for cid in cid_list: 
    try: 
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF" 
 
        response = requests.get(url) 
        if response.status_code == 200: 
           
            filename = f"CID_{cid}.sdf" 
            with open(filename, 'wb') as file: 
                file.write(response.content) 
            print(f"CID {cid} saved as {filename}") 
        else: 
            print(f"Failed to fetch CID {cid}: HTTP {response.status_code}") 
    except Exception as e: 
        print(f"Error fetching CID {cid}: {e}") 
print('done') 