import resource
import sys

class Node:
    def __init__(self, id, value):
        self.value = value
        self.id = id
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


CHARS = "AGTC"

def read_input(infile):
    graph = {}
    indeg = {}
    max_dna_length = 0
    leaf = 1
    with open(infile, 'r') as f:
        for line in f:
            tokens = line.rstrip().split('->')
            if len(tokens) < 2:
                continue
            parent = int(tokens[0])
            child = tokens[1]

            if parent not in graph.keys():
                graph[parent] = Node(parent, "")
            if parent not in indeg.keys():
                indeg[parent] = 0
            p = graph[parent]
            if child.isdigit():
                child = int(child)
                if child not in graph.keys():
                    graph[child] = Node(child, "")
                c = graph[child]
                if child not in indeg.keys():
                    indeg[child] = 0
                indeg[child] += 1
                if p.left == None:
                    p.left = c
                else:
                    p.right = c
            else:
                graph[-leaf] = Node(-leaf, child)
                max_dna_length = max(max_dna_length, len(child))
                if p.left == None:
                    p.left = graph[-leaf]
                else:
                    p.right = graph[-leaf]
                leaf += 1
    return graph, indeg, max_dna_length

dp = {}
state = {}

def solve(graph, nodeId, curChar, x):
    if (nodeId, curChar) in dp.keys():
        return dp[(nodeId, curChar)]
    node = graph[nodeId]
    if node.id < 0:
        return 0 if curChar == node.value[x] else 1
    minVal = 10**12
    minlc = ""
    minrc = ""
    for lc in CHARS:
        for rc in CHARS:
            lval = solve(graph, node.left.id, lc, x)
            rval = solve(graph, node.right.id, rc, x)

            curVal = lval + rval
            if lc != curChar: curVal += 1
            if rc != curChar: curVal += 1

            if curVal < minVal:
                minVal = curVal
                minlc = lc
                minrc = rc
    
    dp[(nodeId, curChar)] = minVal
    state[(node.left.id, curChar)] = minlc
    state[(node.right.id, curChar)] = minrc
    return minVal

def build(graph, nodeId, curChar):
    node = graph[nodeId]
    if node.id < 0:
        return
    node.value += curChar
    build(graph, node.left.id, state[(node.left.id, curChar)])
    build(graph, node.right.id, state[(node.right.id, curChar)])

def ham(a, b):
    dist = 0
    for l, r in zip(a,b):
        if l != r:
            dist += 1
    return dist

def printTree(graph, parent, child):
    cnode = graph[child]
    if parent != 0:
        pnode = graph[parent]
        print cnode.value+"->"+str(pnode.value)+":"+str(ham(cnode.value, pnode.value))
        print pnode.value+"->"+str(cnode.value)+":"+str(ham(cnode.value, pnode.value))

    if cnode.id > 0:
        printTree(graph, child, cnode.left.id)
        printTree(graph, child, cnode.right.id)
        


sys.setrecursionlimit(0x100000)

graph, indeg, max_dna_length = read_input("rosalind_ba7f1.txt")
root = None
for key in graph.keys():
    if key > 0 and indeg[key] == 0:
        root = key
ans = 0
for i in range(max_dna_length):
    minVal = 10**18
    minChr = ""
    dp = {}
    state = {}   
    for c in CHARS:
        val = solve(graph, root, c, i)
        if val < minVal:
            minVal = val
            minChr = c
    build(graph, root, minChr)
    #print (i, minVal)
    ans += minVal

print ans
printTree(graph, 0, root)