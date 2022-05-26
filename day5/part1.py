with open('input.txt') as stroks:
    stroks = stroks.read().split('\n')



spis = []
for i in stroks:
    k=0
    for letter in i:
        if letter in 'aeiou':
            k+=1
            print(k)
    if k >= 3:
        spis.append(i)

spis2=[]
for p in spis:
    d = 0
    for i,j in zip(p,p[1:]):
        if i == j:
            d+=1
    if d > 0:
        spis2.append(p)

spis3=[]
for z in spis2:
    g = 0
    for i,k in zip(z, z[1:]):
        if i+k == 'ab' or i+k == 'cd' or i+k == 'pq' or i+k == 'xy':
            g +=1
    if g == 0:
        spis3.append(z)

print(len(spis3))

with open('output1.txt', 'a') as file:
    file.write(str(len(spis3)))








