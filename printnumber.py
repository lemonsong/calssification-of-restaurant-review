a=open('12opentable_train20000.txt')
for line in a:
    line=line.split('\t')
    words=line[0].split()
    for n in range(0,len(words)-1):
        try:
            num=int(words[n])
            print num, words[n+1],str(line[1])
        except ValueError:
            continue