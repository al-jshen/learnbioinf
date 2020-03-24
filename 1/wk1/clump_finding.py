with open('./E_coli.txt', 'r') as f:
    dat = f.read().split('\n')
txt = dat[0]
#k, L, t = [int(i) for i in dat[2].split(' ')]
k, L, t = (9, 500, 3)

valids = set()
cts = {}

initialwin = txt[:L]
for i in range(len(initialwin) - k + 1):
    kmer = initialwin[i:i+k]
    if kmer not in cts.keys():
        cts[kmer] = 1
    else:
        cts[kmer] += 1
    if cts[kmer] >= t:
        valids.add(kmer)


for i in range(len(txt) - L + 1):
    window = txt[i:i+L+1]
    first = window[:k]
    last = window[-k:]
    cts[first] -= 1
    if last not in cts.keys():
        cts[last] = 1
    else:
        cts[last] += 1
    if cts[last] >= t:
        valids.add(last)

print(len(valids))
