with open('input.txt') as stroks:
    stroks = stroks.read().split('\n')

spis=[]
for i in stroks:
    f = 0
    for k,x in zip(i, i[1:]):
        if i.count(k+x) > 1:
            f += 1
    if f > 0:
        spis.append(i)
print(len(spis))


spis2=[]
for z in spis:
    d=0
    for j,k in zip(z, z[2:]):
        if j == k:
            d+=1
    if d>0:
        spis2.append(z)
print(len(spis2))

with open('output2.txt', 'a') as file:
    file.write(str(len(spis2)))