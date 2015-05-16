# -*- coding: utf-8 -*-
"""
Created on Sun Mar 08 15:31:08 2015

@author: Rui
"""
"""
This script retrieves the urls that correspond to restaurants profiles on yelp.com
Here is an example url:
    http://www.yelp.com/biz/st-george-tavern-new-york
    
On the website, restaurants are viewed in pages (10 per page). For example, 
page 1 is http://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan%2C+NY&ns=1#start=0
page 2 is http://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan%2C+NY&ns=1#start=10
etc.

Open a web browser (e.g. chrome) and go to page 1: http://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan%2C+NY&ns=1#start=0.
Right click on the name of the 1st restaurant and click 'Copy Link Address'. If you do this for name 'St. George Tavern',
the link http://www.yelp.com/biz/st-george-tavern-new-york is copied. This is the link to the restaurant's full profile. We want to get
all this link of multiple restaurants and store them in a file.

Our scipct will browse page by page, and retrieve the links of the 10 freelancers in each page.
"""

#import the two libraries we will be using in this script
import urllib2,re


#make a new browser, this will download pages from the web for us. This is done by calling the 
#build_opener() method from the urllib2 library
browser=urllib2.build_opener()

#desguise the browser, so that websites think it is an actual browser running on a computer
browser.addheaders=[('User-agent', 'Mozilla/5.0')]


#number of pages you want to retrieve 
pagesToGet=10


#create a new file, which we will use to store the links to the freelancers. The 'w' parameter signifies that the file will be used for writing.
fileWriter=open('restaurants.txt','w')


#for every number in the range from 1 to pageNum+1  
for page in range(1,pagesToGet+1):
    
    print 'processing page :', page
    
    #make the full page url by appending the page num to the end of the standard prefix
    #we use the str() function because we cannot concatenate strings with numbers. We need
    #to convert the number to a string first.
    url='http://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan%2C+NY&ns=1#start='+str(page*10-10)
    print url

    #use the browser to get the url.
    response=browser.open(url)    
    
    #read the response in html format. This is essentially a long piece of text
    myHTML=response.read()

    #unique=set()#remember unique usernames	

    names=re.findall('<a class="biz-name" href="/biz/(.*?)"',myHTML,re.S)#get all the matches
	
    #for name in names:
	 #   restaurant_name=name.group(1) # get the restaurant name
	  #  if restaurant_name.find('%')==-1:unique.add(restaurant_name) #check to avoid adding the <%- username %>.html construct

    #write the results
    #for restaurant_name in unique:
    fileWriter.write('http://www.yelp.com/biz/'+str(names)+'\n')


#close the file. File that are opened must always be closed to make sure everything is actually written and finalized.
fileWriter.close()


