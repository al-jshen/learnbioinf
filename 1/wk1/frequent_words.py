with open('./dataset_2_10.txt', 'r') as f:
    dat = f.read().split('\n')
txt = dat[0]
k = int(dat[1])
cts = {}
for i in range(len(txt) - k):
    kmer = txt[i:i+k]
    if kmer not in cts.keys():
        cts[kmer] = 1
    else:
        cts[kmer] += 1
maxk = max(cts.values())
maxkmers = [k for k, v in cts.items() if v == maxk]
print(' '.join(maxkmers))
