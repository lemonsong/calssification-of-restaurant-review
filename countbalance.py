file=open('ot_train20000another copy.txt')
a=0
b=0
for line in file:
    line=line.strip().split('\t')
    if line[1]=='0':
        a=a+1
    elif line[1]=='1':
        b=b+1
print a
print b