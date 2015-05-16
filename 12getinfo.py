#!/usr/local/bin/python
# coding: utf-8
# import the libraries we will be using
import urllib2,os,re,sys

# make a new browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

#create a new file, which we will use to store the links to the freelancers. The 'w' parameter signifies that the file will be used for writing.
fileopen=open('12names.txt')
fileinfo=open('12info.txt','w')

"""
Note: The range() function
    the range(a,b) function returns the list of numbers from a all the way to (but excluding) b. 
    For example, range (1,4) will return  [1, 2, 3]
"""

for line in fileopen:
    line = line.strip()
    line = line.split("@@")
    url = 'http://www.opentable.com/' + str(line[1])
    #use the browser to get the url.
    
        
    try:
        act=browser.open(url)
    except urllib2.HTTPError:  # handling exotic HTTP errors
        continue

    #read the response in html format. This is essentially a long piece of text
    myHTML=act.read()

    rate = re.findall('reviews-overall-score.><h1>([0-9.]{1,})',myHTML)
    numreview = re.findall('reviewCount">([0-9]{1,})</span> reviews',myHTML)
    type = re.findall('profile-header-meta-item.>([A-Za-z/ \t\r\n\f\v]+)</li>',myHTML)
    price = re.findall('Price Range:</span><br><span>([A-Za-z0-9$ \t\r\n\f\v]+)</span>',myHTML)
    
    if rate + numreview == []:  # no rate and no numreview
        continue
    elif rate == []: # no rate -> the website has not yet generate rate for this restaurant
        rate = ['N/A']
    else:            # has only 1 review, which was exclue in regular expression for numreview
        numreview = ['1']
    
    fileinfo.write(str(line[0]) + "@@" + str(url) + "@@"+ str(rate[0]) + "@@" + str(numreview[0]) + "@@" + str(type[0]) + "@@" + str(price[0]) +'\n')

