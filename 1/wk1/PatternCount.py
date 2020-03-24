with open('./PatternCount.txt', 'r') as f:
    dat = f.read().split('\n')
txt = dat[1]
pat = dat[2]
count = 0
for i in range(len(txt) - len(pat)):
    if txt[i:i+len(pat)] == pat:
        count += 1
print(count)
