#!/usr/local/bin/python
# coding: utf-8
# import the libraries we will be using
import urllib2,os,re,sys,time,datetime

# make a new browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

#create a new file, which we will use to store the links to the freelancers. The 'w' parameter signifies that the file will be used for writing.
fileopen=open('/Users/yilin/Desktop/web/12info.txt')
filereviews=open('/Users/yilin/Desktop/web/12reviews.txt','w')

"""
Note: The range() function
    the range(a,b) function returns the list of numbers from a all the way to (but excluding) b. 
    For example, range (1,4) will return  [1, 2, 3]
"""
# a function to change "a" "an" into 1
def changeone(a):
    if a in ["a","an"]:
        a = 1
    return a
    
for line in fileopen:
    line = line.strip()
    line = line.split("@@")

    n = 1 # record review page
    while n<=2: # change the number to decide when to stop scrapping reviews
    
        url = str(line[1]) + '?page=' + str(n)
        n = n + 1
    
        #use the browser to get the url.
        try:
            act=browser.open(url)
        except urllib2.HTTPError:  # handling exotic HTTP errors
            continue

        #read the response in html format. This is essentially a long piece of text
        myHTML=act.read()

        rates = re.findall('ratingValue\" content=\"([1-5]{1})\"></div></div></div><div class=\"review-stars-results',myHTML) # rate of restaurant in every comments

        reviewtitles = re.findall('review-title\">(.*?)</h4>',myHTML,re.S) # title of review
        
        '''change the format of date'''
        dates = re.findall('Dined ([an0-9]+) hours? ago</span>',myHTML,re.S)  # one type of date of review: e.g.Dined 6 hours ago
        for o in range(len(dates)):
            dates[o] = time.strftime('%Y-%m-%d',time.localtime(time.time()))

        
        datesa = re.findall('Dined ([a0-9]+) days? ago</span>',myHTML,re.S)  # one type of date of review: e.g.Dined 6 days ago
        for p in range(len(datesa)):
            num = changeone(datesa[p])
            datesa[p] = time.strftime('%Y-%m-%d',time.localtime(time.time()-int(num)))
            dates.append(p) # combine list dates and liste datesa

        datesb = re.findall('Dined on ([A-Za-z0-9, \t\r\n\f\v]+)</span>',myHTML)  # one type of date of review: e.g.Dined on February 18, 2015
        for q in datesb:
            #str to date
            t = time.strptime(q, "%B %d, %Y")
            y,m,d = t[0:3]
            q = str(y)+"-"+str(m)+"-"+str(d) # formate dates
            dates.append(q) # combine list dates and liste datesb

        reviews = re.findall('review-content.....(.*?)</p>',myHTML,re.S)  # content of reviews
        reviews2 = []
        for r in range(len(reviews)): 
            reviews[r]= reviews[r].strip() # delete some spaces

        #write into file
        m=0 # record element in lists
        while m < len(rates):
            filereviews.write(str(line[0]) + "@@" + str(rates[m]) + "@@"+ str(reviewtitles[m]) + "@@" + str(dates[m]) + "@@" + str(reviews[m]) +'\n') 
            m = m + 1  
            

               