import sys
sys.setrecursionlimit(5000)

with open('rosalind_pcov.txt', 'r') as f:
    str_list = f.readlines()
    str_list = [x.strip() for x in str_list]

k = len(str_list[0]) - 1
#print len(str_list)

#print str_list

def final(str_list):
	i = str_list[0]
	for j in str_list:
		if j != i and i[-k:] == j[:k] and len(str_list) != 1:
			i = i + j[-1]
			str_list.insert(0,i)
			str_list.remove(j)
			final(str_list)
	return str_list[0]

print final(str_list)[:len(str_list)]