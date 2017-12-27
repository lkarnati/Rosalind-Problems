#str_list = ['TGAT','CATG','TCAT','ATGC','CATC','CATC']

with open('rosalind_dbru.txt', 'r') as f:
    str_list = f.readlines()
    str_list = [x.strip() for x in str_list]
    #print(str_list)



def rev_comp(string):
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

def rev_comp_list(str_list):
    new_list = []
    for i in str_list:
        new_list.append(rev_comp(i))
    return new_list

comb_list1 = str_list + rev_comp_list(str_list)
#comb_list = set(comb_list1)

comb_list = []
for i in comb_list1:
    if i not in comb_list:
        comb_list.append(i)
        a = sorted(comb_list)
#print(a)

for i in a:
    print('('+i[0:-1]+', '+i[1:]+')')