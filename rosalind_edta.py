import sys

def read():
    with open('rosalind_edta.txt', 'r') as f:
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

dp = {}
action = {}

def editDistance(A, B, m, n):
    if m == len(A):
        return (len(B) - n)
    if n == len(B):
        return (len(A) - m)
    if (m,n) in dp.keys():
        return dp[(m,n)]
    if A[m] == B[n]:
        dp[(m,n)] = editDistance(A, B, m+1, n+1)
        action[(m,n)] = "match"
    else:
        a = editDistance(A, B, m, n+1)
        b = editDistance(A, B, m+1, n)
        c = editDistance(A, B, m+1, n+1)
        minVal = min(a, min(b, c))
        if a == minVal: 
            action[(m,n)] = "insertA"
        elif b == minVal: 
            action[(m,n)] = "insertB"
        else: 
            action[(m,n)] = "subs"
        dp[(m,n)] = minVal + 1
    return dp[(m,n)]

def reconstruct(A, B, m, n):
    if m == len(A):
        return ('', '-' * (len(B) - n))
    elif n == len(B):
        return ('-' * (len(A) - m), '')
    act =  action[(m,n)]
    if act == "match" or act == "subs":
        val = reconstruct(A, B, m+1, n+1)
        return (A[m] + val[0], B[n] + val[1])
    elif act == "insertA":
        val = reconstruct(A, B, m, n+1)
        return ('-' + val[0], B[n] + val[1])
    elif act == "insertB":
        val =reconstruct(A, B, m+1, n)
        return (A[m] + val[0], '-' + val[1])
    return ('', '')



seq = read()
sys.setrecursionlimit(5000*5000)
print(editDistance(seq[0], seq[1], 0, 0))
(a,b) = reconstruct(seq[0], seq[1], 0, 0)
a = a.replace("\n","")
b = b.replace("\n","")
print(a)
print(b)