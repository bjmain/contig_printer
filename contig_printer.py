import sys
length1={}
length2={}
switch1=0
switch2=0
D={}

#keep=[]
#for line in open("kraken2_suspicious_contigs.out_sorted"):
#    i=line.strip().split()
#    contig_id = "".join([">",i[0]])
#    keep.append(contig_id)

#print keep
#keep = [ID.strip() for ID in open("contigs_less_than_100kb.out")]
#keep = [ID.strip() for ID in open("contigs_less_than_1Mb.out")]
#keep = [ID.strip() for ID in open("contigs_less_than_500kb.out")]
#keep = [">233502"]
#keep = [">253707"]
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
