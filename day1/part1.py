import string
with open('input.txt') as parenthesis:
    par = parenthesis.read()

i=0
for j in par:
    if j == '(':
        i+=1
    elif j ==')':
        i-=1
i = str(i)
with open('output1.txt', 'a') as file:
    file.write(i)























