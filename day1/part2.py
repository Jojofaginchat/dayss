import string
with open('input.txt') as parenthesis:
    par = parenthesis.read()

Bt = []
a = 0
for b in par:
    if b == '(':
        a+=1
        Bt = Bt+[a]
    elif b ==')':
        a-=1
        Bt = Bt + [a]
print(Bt)
print(Bt.index(-1)+1)
BL=str(Bt.index(-1)+1)

with open('output2.txt', 'a') as file:
    file.write(BL)
