import os
import sys
import getopt
from urllib.request import URLError, HTTPError, ContentTooShortError
from urllib.request import urlretrieve
import time

PROGNAME = os.path.basename(sys.argv[0])
BASE_URL = "https://files.rcsb.org/download"

def usage():
    print(f"""
Usage: {PROGNAME} -f <file> [-o <dir>] [-c] [-p]

 -f <file>: the input file containing a comma-separated list of PDB ids
 -o  <dir>: the output dir, default: current dir
 -c       : download a cif.gz file for each PDB id
 -p       : download a pdb.gz file for each PDB id (not available for large structures)
 -a       : download a pdb1.gz file (1st bioassembly) for each PDB id (not available for large structures)
 -A       : download an assembly1.cif.gz file (1st bioassembly) for each PDB id
 -x       : download a xml.gz file for each PDB id
 -s       : download a sf.cif.gz file for each PDB id (diffraction only)
 -m       : download a mr.gz file for each PDB id (NMR only)
 -r       : download a mr.str.gz for each PDB id (NMR only)
""")
    sys.exit(1)

def download(url, out):
    print(f"Downloading {url} to {out}")
    #result = subprocess.run(['curl', '-s', '-f', url, '-o', out], capture_output=True)
    try:
      urlretrieve(url, out)
      print(f"Successfully downloaded {url}, {out}")
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason} for URL: {url}")
    except URLError as e:
        print(f"URL Error: {e.reason} for URL: {url}")
    except ContentTooShortError as e:
        print(f"Content Too Short Error: {e} for URL: {url}")
    except IOError as e:
        print(f"I/O Error: {e.strerror} for file: {out}")
    except Exception as e:
        print(f"Unexpected Error: {e} for URL: {url}")
    

def main():
    startTime = time.perf_counter()
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "f:o:cpaAxsmr")
    except getopt.GetoptError as err:
        print(err)
        usage()

    listfile = "".strip()
    outdir = "."
    cif = pdb = pdb1 = cifassembly1 = xml = sf = mr = mrstr = False
    print(opts)

    for o, a in opts:
        if o == "-f":
            listfile = a
        elif o == "-o":
            outdir = a
        elif o == "-c":
            cif = True
        elif o == "-p":
            pdb = True
        elif o == "-a":
            pdb1 = True
        elif o == "-A":
            cifassembly1 = True
        elif o == "-x":
            xml = True
        elif o == "-s":
            sf = True
        elif o == "-m":
            mr = True
        elif o == "-r":
            mrstr = True
        else:
            usage()

    if not listfile:
        print("Parameter -f must be provided")
        sys.exit(1)

    with open(listfile, 'r') as f:
        contents = f.read()

    tokens = contents.strip().split(',')

    for token in tokens:
        print(token)
        print(cif, pdb, pdb1, cifassembly1, xml, sf, mr, mrstr)
        if cif:
            download(f"{BASE_URL}/{token}.cif.gz", f"{outdir}/{token}.cif.gz")
        if pdb:
            download(f"{BASE_URL}/{token}.pdb.gz", f"{outdir}/{token}.pdb.gz")
        if pdb1:
            download(f"{BASE_URL}/{token}.pdb1.gz", f"{outdir}/{token}.pdb1.gz")
        if cifassembly1:
            download(f"{BASE_URL}/{token}-assembly1.cif.gz", f"{outdir}/{token}-assembly1.cif.gz")
        if xml:
            download(f"{BASE_URL}/{token}.xml.gz", f"{outdir}/{token}.xml.gz")
        if sf:
            download(f"{BASE_URL}/{token}-sf.cif.gz", f"{outdir}/{token}-sf.cif.gz")
        if mr:
            download(f"{BASE_URL}/{token}.mr.gz", f"{outdir}/{token}.mr.gz")
        if mrstr:
            download(f"{BASE_URL}/{token}_mr.str.gz", f"{outdir}/{token}_mr.str.gz")
    endTime = time.perf_counter()
    result = f"Completed in {endTime - startTime:0.4f} seconds. {len(tokens)} identifiers processed."
    print(result)

    with open("log.txt", "w") as file:
        file.write(result)

if __name__ == "__main__":
    main()