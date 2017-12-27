import operator

with open("rosalind_ba9l.txt","r") as f:
    content = f.readlines()
    #print(content[0])
    content[0] = content[0].replace("\n","")
    patterns = content[1].split()
    #print(patterns)

def LFmap(bw, target):
    totsIndex = dict()
    for i, c in enumerate(bw):
        totsIndex[i] = c
    t = -1
    for key, value in sorted(totsIndex.items(), key=operator.itemgetter(1)):
        #print('%s, %s' % (key, value))
        t += 1
        if key == target:
            break
    return(t)

def BWMatching(lastcol, pattern, LFmap):
    top = 0

    bottom = len(lastcol) - 1
    #print(bottom)
    while(top <= bottom):
        if(len(pattern) > 0):
            symbol = pattern[-1]
            #print(pattern)
            pattern = pattern[:len(pattern)-1]
            if symbol in lastcol[top:bottom+1]:
                #print(symbol,top,bottom)
                topindex = top+lastcol[top:(bottom+1)].index(symbol)
                revstr = lastcol[top:bottom+1][::-1]

                bottomindex = bottom - revstr.index(symbol)
                top = LFmap(lastcol,topindex)
                bottom = LFmap(lastcol,bottomindex)
                #print(top,bottom)
            else:
                return 0
        else:
            return(bottom - top + 1)
    return 0
#print(content[0])
for x in patterns:
    a = BWMatching(content[0], x, LFmap)
    print(a,end = " ")