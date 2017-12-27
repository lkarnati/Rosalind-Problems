dna_name = ''
dna_seq = ''
dna_dict = {}


with open('rosalind_grph.txt') as f:
    for line in f:
        l = line.strip('\n')
        if l[0] == '>':

            if dna_name != '':
                dna_dict[dna_seq] = dna_name
            dna_name = l[1:]
            dna_seq = ''
        else:
            dna_seq = dna_seq + l

    if dna_name != '':
        dna_dict[dna_seq] = dna_name
#print dna_dict

k = 3
for (s,name) in dna_dict.iteritems():
    for (t, name1) in dna_dict.iteritems():
        #print s, t, name, name1, s[-k:], t[:k]
        if s[-k:] == t[:k] and name != name1:
            print name, name1