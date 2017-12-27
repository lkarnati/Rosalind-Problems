listr = []
temp = ''
with open("rosalind_ba9i.txt","r") as f:
    string = f.read().strip()

    #print(string)
    ss = string*2
    for i in range(0,len(string)):
        temp = ss[i:i+len(string)]
        listr.append(temp)
        temp = ''
    #print (listr)
    p = sorted(listr)
    #print(p)
    for x in p:

        print(x[-1],end='')