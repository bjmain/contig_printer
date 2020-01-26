
switch1=0


keep = [">263881"]
#contig_name = "".join(['>',sys.argv[1]])
#keep = [contig_name]
#keep = [contig_name,">252838",">200817",">153461",">209499",">233638",">253198",">233882",">153175",">200971",">251845"]
#keep = ["".join([">",ID.strip()]) for ID in open("contigs_less_than_2MB.out2")]
#print len(keep) 
for line in open("aws_pseudohap.fa"):
	i=line.strip().split()
	if line[0]==">":
		#c=line.strip()
		c=line.strip().split()[0]
		
                if c in keep:
			switch1=1
			print line.strip()
			continue
		else:
			switch1=0
			continue
	if switch1:
		print line.strip()
