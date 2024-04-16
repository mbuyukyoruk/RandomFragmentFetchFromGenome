import argparse
import os
import sys
import subprocess
import re
import pdb
import random
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python RandomFragmentFetchFromGenome.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

# RandomFragmentFetchFromGenome

Author: Murat Buyukyoruk

        RandomFragmentFetchFromGenome help:

This script is developed to fetch random sequences from multifasta file. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        python RandomFragmentFetchFromGenome.py -i demo.fasta -o demo_out_random_regions.fasta -f 200

RandomFragmentFetchFromGenome dependencies:

Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download

tqdm                                                refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file to fetch random regions.)

	-o/--output		output file	    Specify a output file name that should contain fetched random regions.
	
    -f/--flank		length	        Specify length to fetch randomly.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.
	
      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename', help='Specify a fastafile.\n')
parser.add_argument('-o', '--out', required=True, type=str, dest='out', help='Specify a output file.\n')
parser.add_argument('-f', '--flank', required=True, type=str, dest='flank', help='Specify length to fetch randomly.\n')

results = parser.parse_args()
filename = results.filename
out = results.out
flank = results.flank

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

f = open(out, 'a')
sys.stdout = f

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Finding random bg sequences...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        acc = record.id.rsplit('_',2)[0]

        seq = record.seq
        seq_len = len(seq)
        n = random.randint(0,seq_len - int(flank)-1)
        r_start = n
        r_stop = n + int(flank)
        print(">" + record.description)
        print(re.sub("(.{60})", "\\1\n", str(seq[r_start:r_stop]), 0, re.DOTALL))
