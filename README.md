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

	-o/--output		output file		Specify a output file name that should contain fetched random regions.
	
	-f/--flank		length			Specify length to fetch randomly.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.
	
