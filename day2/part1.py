with open('input.txt') as lengthes:
    leng = lengthes.read().split('\n')


mass = []
mass1 = []
for i in leng:
    mass.append(i.split('x'))
a = 0
for k in mass:
    i1 = int(k[0])
    i2 = int(k[1])
    i3 = int(k[2])

    mass1.append(2*i1*i2+2*i2*i3+2*i1*i3+min(i1*i2,i2*i3,i1*i3))

print(sum(mass1))
with open('output1.txt', 'a') as file:
    file.write(str(sum(mass1)))




