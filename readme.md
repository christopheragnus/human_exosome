# Model-based Structure and Dynamics of Protein Complexes.

https://github.com/user-attachments/assets/97273597-f8bb-4e26-9e9a-0c6d58ecd1f3

## Organizations:

The Rockefeller University (New York)
ERIBA (Groningen)

## Departments:
Research Group: Dr. John LaCava

## Supervisors:
Student Supervisor: Dr. Anton Feenstra, Vrije Universiteit (Amsterdam)
Project Supervisor: Dr. Niki Athanasiadou, The Rockefeller University (New York)

## Project Description
The aim of this internship is to evaluate and optimize AlphaFold predictions of the exosome complex. The exosome complex is a crucial ribonucleolytic machine involved in RNA metabolism, degradation, and quality control of various RNA species. 

## How to run files

- `bash_files/main.sh` - this is a wrapper script around the bulk download script `batch_download.sh` downloaded from PDB and then extracts the .gz files into `output/bash_files` and then repeats it five times. Each individual execution time is stored in `execution_times.txt`. It calculates the mean execution time and stores it in `mean_execution_time.txt`. To run this file, run in your terminal, go to the `bash_files` folder and run: `./main.sh 'input/cls4-2.txt'`. (this is the example input file)

- `bash_files/batch_download.sh` - this is the bulk download script from PDB.

- `python_files/python_benchmark.py` - this does the same thing as `main.sh` but using Python code to evaluate whether Python or bash is faster. Extracted PDB files are stored in the output file: `pdb_output_files`. 

- `python_files/main.py` - this downloads data about proteins from the PDB GraphQL API and then parses the save and saves it into `python_files/pdb_metadata` as a JSON file. Two modules are imported `fetch_data` and `parse_data`. The input it takes is a txt file contain comman-separated list of PDB identifiers. To run this file, you need to enter in the terminal in format with the input file: `python main.py -f example.txt`

- `python_files/src/fetch_data.py` - fetches data from the PDB data GraphQL based on the protein identifier. Then it writes the data into a JSON file in `/pdb_metadata` folder.

- `python_files/src/parse_data.py` -  this module indexes the API response, converts it to a Python dictionary and then returns combines id, deposited dates, doi, method, summetry and polymer entities as `summary_table.json`.

- `python_files/query.graphql` - this file contains the GraphQL query used to pull data from the PDB API. This is imported into `fetch_data.py`.


- `python_files/log.txt` - this logs the output from `python_benchmark.py`

- `notebooks/alphafold-analysis.ipynb` - this is the main notebook containing the AlphaFold's prediction analysis. It also contains some functions which generates the `subunits.json` for CombFold and the summary table output.

- `notebooks/output/output.csv` - this is the summary table output.

- `/mnt/users/chris01/combfold-outputs-final` - folder of the predicted proteins 

- The presentation link: `https://macromolecule.slack.com/archives/C01168ZG1UN/p1730128534363199`

### Youtube Link:
[Watch the video](https://youtu.be/cxPRnBBW28g)

### Google Presentation:
[View the presentation](https://docs.google.com/presentation/d/1PfBp83GXRjB78-rTCtF8Tr1gZx9IAdsa-4kPZFKnWW8/edit?usp=sharing)

```
Future research directions:
Suggestions I made at the end - if unhappy with CombFold quality on human exosome -
yeast exosome
archaebacterial exosome
eubacterial ‘degradasome’ or PNPase or RNase PH trimer
^^ these are in terms of decreasing complexity and multimer number in the complex

https://docs.google.com/presentation/d/1PfBp83GXRjB78-rTCtF8Tr1gZx9IAdsa-4kPZFKnWW8/edit?usp=sharing
18:16 - Combfold spits out files that need to go into AlphaFold but don't have the correct FASTA syntax.  - yep, it generates the pairs but adds a colon to the file. I think its because the authors themselves were using ColabFold "which uses colons to specify inter-protein chainbreaks for modeling complexes" For example PI...SK:PI...SK for a homodimer.
See;https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
Definitely confusing because using it with Little_beast's AlphaFold would throw up errors about it.
20:34 - what distinguishes CombFold from AlphaFold-multimer? what's the secret sauce injected by CombFold minus the AF contribution?
- CombFold combines AF2 with a deterministic combinatorial assembly algorithm but does not replace AlphaFold itself.
- CombFold, uses a small number of pairwise subunit interactions generated by AlphaFold2 for assembly instead of thousands generated by docking. The hierarchical and combinatorial assembly stage exhaustively enumerates possible assembly trees, maximizing the probability of correctly assembling the complex based on pairwise AlphaFold2 interactions (combinatorial enumeration). See figure 5 in the paper
- CombFold allows integration of distance restraints from crosslinking mass spectrometry to generate structures at a higher success rate. Paper mentions "on the benchmark of homomeric complexes used for MoLPC validation and obtain a top-1 success rate of 57%. CombFold successfully assembles six out of seven CASP15 targets with over 3,000 amino acids".
https://www.nature.com/articles/s41592-024-02174-0
22:35 - I'm definitely use human sequences, not yeast. I used the general name for the sequence after the supplementary paper attached the 2NN6 exosome complex. You have to name it something "easy" or else you get errors with naming the string in the subunits.json file.
https://www.sciencedirect.com/science/article/pii/S0092867406014279?via%3Dihub
Also - the sequence coverage drops off at the extreme ends of the positions for each of the predicted protein pairs. I think this is the cause of the ends of the protein going all random directions at the ends?

```
Source: [Slack Link](https://macromolecule.slack.com/archives/C01168ZG1UN/p1730128534363199)
