file=open('yelpresultchicago_1.txt')
w=open('yelpbalancechicago_1.txt','w')
n=0

for line in file:        
    n=n+1
    if n<=9700:
        w.write(line)
    
    
