with open('./dataset_3_2.txt', 'r') as f:
    dat = f.read().split('\n')
dat = dat[0]
pairs = {
    'G': 'C',
    'C': 'G',
    'A': 'T',
    'T': 'A'
}
newstr = ''.join([pairs.get(i) for i in dat])
print(newstr[::-1])
