with open('./dataset_2_7.txt', 'r') as f:
    dat = f.read().split('\n')
txt = dat[0]
pat = dat[1]
count = 0
for i in range(len(txt) - len(pat)):
    windpat = txt[i:i+len(pat)]
    print(windpat)
    if windpat == pat:
        count += 1
print(count)
