from math import log

with open('rosalind_prob.txt', 'r') as f:
    content = f.readlines()

dna_string = content[0]
prob_list = list(map(float, (content[1].split())))

result = ""
for i in prob_list:
    temp = []
    for s in dna_string:
        if s == 'A' or s == 'T':
            temp.append((1-i)/2)
        if s == 'G' or s == 'C':
            temp.append(i/2)
    #print(temp)
    new_temp = []
    new_temp = [log(y,10) for y in temp]

    q = round(sum(new_temp),3)
    result = result + " " + str(q)

print (result)