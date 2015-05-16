file=open('ot_train20000.txt')
neg=0
pos=0
for line in file:
    a=0
    line=line.lower()
    line=line.split('\t')
    #print line[0]
    #print type(line[1])
    words=line[0].split(' ')
    #print words
    a=words.count("least")
    print a,str(line[1])
    if line[1]=='1':
        pos=pos+a
        print 'pos'
    elif line[1]=='0':
        neg=neg+a
print "neg",neg
print "pos",pos