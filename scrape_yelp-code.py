# -*- coding: utf-8 -*-


import urllib2,os,re,sys

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

yelpresult1=open('yelpresultmadison_1.txt','w')
yelpresult0=open('yelpresultmadison_0.txt','w')

userpagesToGet=20
reviewpagesToGet=151

for n in range(0,userpagesToGet):
    url1 = 'http://www.yelp.com/search?find_desc=Restaurants&find_loc=Madison%2C+WI&start='+str(n*10)+'#start='+str(n*10)
    try:
        response=browser.open(url1)
    except urllib2.HTTPError:
        continue
    userspage=response.read()
    names = re.finditer('search-result" data-key=(.*?)<p class="snippet">',userspage,re.S)
    for rmatch in names:
        name=re.search('<a class="biz-name" href="(.*?)" data-hovercard-id="(.*?)">(.*?)</a>',rmatch.group(1)).group(3)
        
        eadd=re.search('<a class="biz-name" href="(.*?)" data-hovercard-id="(.*?)">(.*?)</a>',rmatch.group(1)).group(1)
        
        for i in range(0,reviewpagesToGet):
            url2='http://www.yelp.com'+eadd+'?start='+str(i*40)+'&sort_by=rating_asc'
            try:
                act=browser.open(url2)
            except urllib2.HTTPError:
                continue
            myHTML=act.read()
                     
            reviewMatches=re.finditer('<div class="review-wrapper">(.*?)<p itemprop="description" lang="(.*?)<div class="review-footer clearfix">',myHTML,re.S)
                        
            for rmatch in reviewMatches:
                text=re.search('">(.*?)</p>',rmatch.group(2)).group(1).replace("&#39;","'").replace("<br><br>"," ").replace("\n"," ").replace("<br>"," ").replace("&#34;",'"')
                rate=re.search('<meta itemprop="ratingValue" content="(.*?)">',rmatch.group(1)).group(1)
                #date=re.search('<meta itemprop="datePublished" content="(.*?)">',rmatch.group(1)).group(1).replace("\n"," ")
                
                if rate=='4.0' or rate=='5.0':
                    rate2='1'
                    yelpresult1.write(text+'\t'+str(rate2)+'\n')

                elif rate=='1.0' or rate=='2.0':
                    rate2='0'
                    yelpresult0.write(text+'\t'+str(rate2)+'\n')

                
            
            
yelpresult0.close() 
yelpresult1.close() 