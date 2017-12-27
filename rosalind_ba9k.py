import operator

with open("rosalind_ba9k.txt","r") as f:
    file_input = f.read().strip();
    bw = file_input.splitlines()[0]
    target = int(file_input.splitlines()[1])

    #print(bw)
    #print(target)

    totsIndex = dict()
    for i, c in enumerate(bw):
        totsIndex[i] = c
    t = -1
    for key, value in sorted(totsIndex.items(), key=operator.itemgetter(1)):
        #print('%s, %s' % (key, value))
        t += 1
        if key == target:
            break

    print(t)