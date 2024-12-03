# fetch data from PDB graphql, download as JSON and process as CSV for Jupter import

import requests
import json

def read_query_from_file(filename):
  with open(filename, 'r') as file:
    return file.read()

url = "https://data.rcsb.org/graphql"

query = read_query_from_file('query.graphql')

headers = {
  'Content-Type': 'application/json'
}

# fetch data from GraphQL API
def fetch_data(id):
  payload = {
    "query" : query,
    "variables": { "id": id }
  }

  response = requests.post(url, json=payload, headers=headers)

  if response.status_code == 200:
    data = response.json()
    with open(f'./pdb_output_files/{id}.json', 'w') as json_file:
      json.dump(data, json_file, indent=4)
    print(data)
  else:
    print('Response failed.')
    print(response.text)


  