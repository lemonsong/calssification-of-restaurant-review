text=open('yelpresult3.txt')
yelpresult0=open('yelpresultchicago_0.txt','w')
yelpresult1=open('yelpresultchicago_1.txt','w')
for line in text:
    line=line.strip().split('\t')
    if line[1]=='0':
        yelpresult0.write(str(line[0])+'\t'+str(line[1])+'\n')
    elif line[1]=='1':
        yelpresult1.write(str(line[0])+'\t'+str(line[1])+'\n')
