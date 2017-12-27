dna = ''
introns = []
temp = ''

with open('rosalind_splc.txt','r') as f:
    lines = f.read().splitlines()
    #print lines
    for line in lines:     	
        if "Rosalind" in line:
        	introns.append(temp)
	    	temp = ''
	    	continue
        temp = temp + line

introns.append(temp)

dna = introns[1]


#print "dna after removal"
for i in range(2,len(introns)):
	#print introns[i]
	dna = dna.replace(introns[i],"")

#print dna

DNA_LOOKUP_TABLE = {'TTT': 'F','CTT': 'L',     'ATT': 'I',     'GTT': 'V','TTC': 'F','CTC': 'L',     'ATC': 'I',     'GTC': 'V',
'TTA': 'L','CTA': 'L',     'ATA': 'I',     'GTA': 'V',
'TTG': 'L','CTG': 'L',     'ATG': 'M',     'GTG': 'V',
'TCT': 'S','CCT': 'P',     'ACT': 'T',     'GCT': 'A',
'TCC': 'S','CCC': 'P',     'ACC': 'T',     'GCC': 'A',
'TCA': 'S','CCA': 'P',     'ACA': 'T',     'GCA': 'A',
'TCG': 'S','CCG': 'P',     'ACG': 'T',     'GCG': 'A',
'TAT': 'Y','CAT': 'H',     'AAT': 'N',     'GAT': 'D',
'TAC': 'Y','CAC': 'H',     'AAC': 'N',     'GAC': 'D',
'TAA': '','CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
'TAG': '','CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
'TGT': 'C','CGT': 'R',     'AGT': 'S',     'GGT': 'G',
'TGC': 'C','CGC': 'R',     'AGC': 'S',     'GGC': 'G',
'TGA': '','CGA': 'R',     'AGA': 'R',     'GGA': 'G',
'TGG': 'W','CGG': 'R',     'AGG': 'R',     'GGG': 'G'}



#dna = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'
temp = ''
for n in range(0, len(dna)-2, 3):
	temp = temp + DNA_LOOKUP_TABLE[dna[n:n+3]]
	#print DNA_LOOKUP_TABLE[dna[n:n+3]],dna[n:n+3]

print temp