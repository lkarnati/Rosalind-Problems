with open('rosalind_mrna.txt') as f:
   prot = f.read(); 
frequency = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'STOP': 3
}
prot = prot.strip()
prot = list(prot)
product = 1
for i in prot:
    product *= frequency[i]%1000000
print ((product*(3%1000000))%1000000)