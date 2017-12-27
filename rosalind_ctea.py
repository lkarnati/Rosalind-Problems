import sys

def read():
    with open('rosalind_ctea.txt', 'r') as f:
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
    #print(seq)
    seq[0].strip()
    seq[1] = seq[1].replace('\n', '')
    #seq[1].strip()
    #print(seq[0])
    #print(seq[1])
    #print("Seq 0 len",len(seq[0]))
    #print("Seq 1 len",len(seq[1]))
    return seq

MOD = (2**27) - 1
dp = {}

def editDistance(A, B, m, n):
    if m == 0:
        return (n,1)
    if n == 0:
        return (m,1)
    if (m,n) in dp.keys():
        return dp[(m,n)]
    a = editDistance(A, B, m, n-1)
    b = editDistance(A, B, m-1, n)
    c = editDistance(A, B, m-1, n-1)
    val = c[0]
    if A[m-1] == B[n-1]:
        val = c[0] - 1
    minVal = min(a[0], min(b[0], val))
    ctx = 0
    if a[0] == minVal: ctx += a[1]
    if b[0] == minVal: ctx += b[1]
    if val == minVal: ctx += c[1]
    dp[(m,n)] = (minVal + 1, ctx%MOD)
    return dp[(m,n)]

seq = read()
sys.setrecursionlimit(5000*5000)
print (editDistance(seq[0], seq[1], len(seq[0]), len(seq[1]))[1])