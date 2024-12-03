# parse json and save in one file

import json
import os

def find_json_files(directory):
  json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
  return json_files

summary_table = {}


def read_json_file(json_files):
  
  for file in json_files: 
    print(json_files)
    
    with open(f'./pdb_output_files/{file}', 'r') as json_file:
      data = json.load(json_file)
      # this is the indexing function
      parsed_data =  {
          "id" : data["data"]["entry"]["rcsb_id"],
          "deposited": data["data"]["entry"]["rcsb_accession_info"]["deposit_date"],
          # "doi": data["data"]["entry"]["pubmed"]["rcsb_pubmed_doi"],
          "method" : data["data"]["entry"]["refine"],
          "symmetry": data["data"]["entry"]["assemblies"],
          "polymer_entities": data["data"]["entry"]["polymer_entities"]
          }
      summary_table[parsed_data["id"]] = parsed_data
      

def main():
  list_of_files = find_json_files("pdb_output_files")
  read_json_file(list_of_files)
  with open(f'./summary_table.json', 'w') as json_file:
      json_object = json.dumps(summary_table, indent=4)
      json_file.write(json_object)

# print(summary_table)


     




