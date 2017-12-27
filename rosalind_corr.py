with open("rosalind_corr.txt","r") as f:
    str_list =[]
    for line in f:
        if(line[0] != '>'):
            str_list.append(line.strip())

# print(string_list)

def hamming(string1, string2):
    hdist = 0
    for i in range(0, len(string1)):
        if(string1[i] != string2[i]):
            hdist = hdist + 1
    return hdist
#print(hamming('ACC','AGG'))

def reverse(string):
    rev = string[::-1]
    dict = {'A' : 'T',
            'T' : 'A',
            'C' : 'G',
            'G' : 'C'}
    complist =[]

    for i in rev:
        complist.append(dict[i])
    comp = ''.join(complist)
    return comp
    #print(comp)


def occurcount(str_list):
	count_dict = {}
	for i in range(len(str_list)):
		if str_list[i] in count_dict.keys():
			count_dict[str_list[i]] = count_dict[str_list[i]] + 1
		elif reverse(str_list[i]) in count_dict.keys():
			count_dict[reverse(count_dict[i])] = count_dict[reverse(count_dict[i])] + 1
		else:
			count_dict[str_list[i]] = 1
			count_dict[reverse(str_list[i])] = 1

	return count_dict


#print occurcount(str_list)

def answer():
	check_dict = occurcount(str_list)
	right = []
	for i in check_dict.keys():
		if check_dict[i] > 1:
			right.append(i)

	wrong = []
	for i in check_dict.keys():
		if check_dict[i] == 1:
			wrong.append(i)
	#print right, wrong

	corr = []

	for i in wrong:
		for j in right:
			if hamming(i,j) == 1:
				print i+'->'+j
				#corr.append([i,j])
	#return corr

answer()