import sys

# python 2

switch=0
# You need to update this keep list with your contigs of interest.
keep = [">tig00032677"]

# input your fasta file after the python script: python print_contig.py genome.fa
for line in open(sys.argv[1]):
	i=line.strip().split()
	if line[0]==">":
		c=line.strip().split()[0]
                if c in keep:
			switch=1
			#print(line.strip()) # Switch to this line if you are using python3
			print line.strip()
			continue
		else:
			switch=0
			continue
	if switch:
		print line.strip()
                #print(line.strip()) # Switch to this line if you are using python3
