#!/usr/local/bin/python
# coding: utf-8
# import the libraries we will be using
import urllib2,os,re,sys

# make a new browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

#create a new file, which we will use to store the links to the freelancers. The 'w' parameter signifies that the file will be used for writing.
#fileopen=open('/Users/yilin/Desktop/web/9companylist.txt')
restaurantsnames=open('12names.txt','w')

"""
Note: The range() function
    the range(a,b) function returns the list of numbers from a all the way to (but excluding) b. 
    For example, range (1,4) will return  [1, 2, 3]
"""
#fileWriter.write("mother company@@relation@@child company name@@website@@type@@location@@rate@@introduction"+'\n')


url1 = 'http://www.opentable.com/new-york-restaurant-listings?metroid=8&regionids=16&sort=Name&size=100&excludefields=description&from=000'

#use the browser to get the url.
response=browser.open(url1)    
#read the response in html format. This is essentially a long piece of text
myHTML=response.read()

# if you want to scrape until the last page, use the following code
# end = re.findall('js-pagination-page pagination-link\" data-from=\"\d+\">(\d+)',myHTML)
# last page: int(end[-1]) 

n=1  #record current page
while n <= 2: # change the number to decide when stop scrapping
    url2 = 'http://www.opentable.com/new-york-restaurant-listings?metroid=8&regionids=16&sort=Name&size=100&excludefields=description&from='+str(n-1)+'00'
    
    try:
        response=browser.open(url1)
    except urllib2.HTTPError:  # handling exotic HTTP errors
        continue
        
    listpage=response.read()

    names = re.finditer('<div class="result content-section-list-row cf"(.*?)<a href="/(.*?)</a>',listpage,re.S)#get all the matches
    
    for rmatch in names:
        rid=re.search('data-rid="(.*?)" data-offers=',rmatch.group(1)).group(1) # restaurant id
        name=re.search('(.*?)" class="rest-row-name rest-name">',rmatch.group(2)).group(1) # restaurant name
        restaurantsnames.write(rid+'@@'+name+'\n')
        
    n = n+1

restaurantsnames.close()