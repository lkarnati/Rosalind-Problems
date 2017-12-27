import resource
import sys

def read_input(infile):
    graph = {}
    indeg = {}
    outdeg = {}
    with open(infile, 'r') as f:
        for line in f:
            tokens = line.split(' -> ')
            node = int(tokens[0])
            l = [int(x) for x in tokens[1].split(',')]
            graph[node] = l
            outdeg[node] = len(l)
            if node not in indeg.keys():
                indeg[node] = 0
            for x in l: 
                if x not in indeg.keys(): 
                    indeg[x] = 0
                if x not in graph.keys():
                    graph[x] = []
                if x not in outdeg.keys():
                    outdeg[x] = 0
            for x in l: indeg[x] += 1
    return graph, indeg, outdeg
    
def check(graph, visited, cur, dest):
    visited.add(cur)
    found = False
    for v in graph[cur]:
        if v == dest:
            return True
        if v not in visited:
            found = found or check(graph, visited, v, dest)
    return found

            

def solve(graph, visited, soln, node):
    last = -1
    if len(graph[node]) == 0:
        soln.append(node)
    adj = list(graph[node])
    for v in adj:
        if (node, v) in visited:
            continue
        if check(graph, set(), v, node):
            soln.append(node)
            visited.add((node,v))
            graph[node].remove(v)
            solve(graph, visited, soln, v)
        elif last == -1:
            last = v
        else:
            raise('Apocalypse is here')

    if last != -1 and (node, last) not in visited:
        soln.append(node)
        visited.add((node,last))
        solve(graph, visited, soln, last)

    

sys.setrecursionlimit(0x100000)

graph, indeg, outdeg = read_input('rosalind_ba3g.txt')
soln = []
for v in graph.keys():
    if outdeg[v] > indeg[v]:
        solve(graph, set(), soln, v)
        print ('->'.join(str(x) for x in soln))