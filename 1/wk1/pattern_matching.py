with open('./Vibrio_cholerae.txt', 'r') as f:
    dat = f.read().split('\n')
#pat = dat[0]
pat = 'CTTGATCAT'
genome = dat[0]
idxs = []
for i in range(len(genome) - len(pat)):
    if genome[i:i+len(pat)] == pat:
        idxs.append(i)
print(*sorted(idxs), sep=' ') # i learned something new
