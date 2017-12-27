import sys

def read():
    with open('rosalind_mgap.txt', 'r') as f:
        seq = []
        currentSeq = ""
        for line in f:
            if line[0] == '>' and len(currentSeq):
                seq.append(currentSeq.replace('\n',''))
                currentSeq = ""
            elif line[0] != '>':
                currentSeq = currentSeq + line
        if len(currentSeq):
            seq.append(currentSeq)
    seq[0].strip()
    seq[1] = seq[1].replace('\n', '')
    #print(seq[0])
    #print(seq[1])
    return seq

dp = {}

def editDistance(A, B, m, n):
    if m == 0:
        return (n,n)
    if n == 0:
        return (m,m)
    if (m,n) in dp.keys():
        return dp[(m,n)]
    if A[m-1] == B[n-1]:
        dp[(m,n)] = editDistance(A, B, m-1, n-1)
    else:
        a = editDistance(A, B, m, n-1)
        b = editDistance(A, B, m-1, n)
        minVal = min(a[0], b[0])
        ctx = 0
        if a[0] == minVal: ctx = a[1]
        if b[0] == minVal: ctx = max(ctx,b[1])
        dp[(m,n)] = (minVal + 1, ctx + 1)
    return dp[(m,n)]

seq = read()
sys.setrecursionlimit(5000*5000)

print (editDistance(seq[0], seq[1], len(seq[0]), len(seq[1]))[0])