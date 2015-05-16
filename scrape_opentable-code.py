# -*- coding: utf-8 -*-
"""
Team member: Sanchuan Hu, Yilin Wei, Rui Xue, Yijing Mao
"""

import urllib2,re,time,datetime

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

Tresult0=open('othouston0.txt','w')
Tresult1=open('othouston1.txt','w')


userpagesToGet=18
#reviewpagesToGet=1000

for n in range(0,userpagesToGet):
    print 'user page:'+str(n+1)
    url1 = 'http://www.opentable.com/houston-restaurants-listings?metroid=8&regionids=16&sort=Name&size=100&from='+str(n*100)+'&excludefields=description'+str(n*10)
    try:
        response=browser.open(url1)
    except urllib2.HTTPError: # handling exotic HTTP errors
        continue
    userspage=response.read()
    names = re.finditer('<div class="result content-section-list-row cf"(.*?)<a href="/(.*?)</a>',userspage,re.S) # get name of the restaurant
    for rmatch in names:
        name=re.search('(.*?)" class="rest-row-name rest-name">',rmatch.group(2)).group(1) # get name of the restaurant
        
        ID=re.search('data-rid="(.*?)" data-offers=',rmatch.group(1)).group(1) # restaurant id
        
        #get number of review pages
        url2='http://www.opentable.com/'+name+'?page='+'1' # go into the restaurant website
        try:
            act=browser.open(url2)
        except urllib2.HTTPError: # handling exotic HTTP errors
            continue
        pageHTML=act.read()
        reviewpagesToGet=re.findall('data-page=.([0-9]{1,}). class=.pagination-link.>\d+</a>',pageHTML)
        if reviewpagesToGet==[]:
            reviewpagesToGet=['1']
        print reviewpagesToGet
            
        for i in range(0,int(reviewpagesToGet[-1])):
            print name+' reviewpage:'+str(i+1)
            url3='http://www.opentable.com/'+name+'?page='+str(i+1) # go into the restaurant website
            try:
                act=browser.open(url3)
            except urllib2.HTTPError: # handling exotic HTTP errors
                continue
            myHTML=act.read()
                        
            reviewMatches=re.finditer('itemprop="reviewRating"(.*?)itemprop="itemReviewed',myHTML,re.S)
                        
            for rmatch in reviewMatches:
                text=re.search('class="review-content"><p>(.*)</p>',rmatch.group(1),re.S).group(1).replace("&#39;","'").replace("<br><br>"," ").replace("\n"," ").replace("<br>"," ").replace("&#34;",'"')
                rate=re.search('" title="(.*)" class="all-stars filled"',rmatch.group(1),re.S).group(1).replace("\n"," ")
                date=re.search('class="color-light">(.*)</span></div><div',rmatch.group(1),re.S).group(1).replace("\n"," ")
                title=re.search('class="review-title">(.*)</h4><div',rmatch.group(1),re.S).group(1).replace("\n"," ")
                if int(rate)==3:
                    continue
                elif int(rate)>3:
                    rate2=1
                    Tresult1.write(text+'\t'+str(rate2)+'\n')

                else:
                    rate2=0
                    Tresult0.write(text+'\t'+str(rate2)+'\n')

                # code to get all information
                #OTresult.write('Restaurant Name: '+name+'\t'+'ID: '+ID+'\t'+'Review time: '+date+'\t'+'Rate: '+rate+'\t'+'Title: '+title+'\t'+'Review: '+text+'\n\n')

            
print 'end'
Tresult1.close() 
Tresult0.close() 