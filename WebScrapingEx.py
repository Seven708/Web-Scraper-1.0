
##Jeremiah D. Johnson - Written & modified to pull from certain websites for RSS feed

##from urllib.request import urlopen
##html = urlopen("http://www.chase.com/news.html")
##print(html.read())


##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##
##html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
##bsObj = BeautifulSoup(html.read());
##print(bsObj.h1)







## #getExternalLinks.py
##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##import re
##import datetime
##import random
##
##pages = set()
##random.seed(datetime.datetime.now())
##
###Retrieves a list of all Internal links found on a page
##def getInternalLinks(bsObj, includeUrl):
##    internalLinks = []
##    #Finds all links that begin with a "/"
##    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
##        if link.attrs['href'] is not None:
##            if link.attrs['href'] not in internalLinks:
##                internalLinks.append(link.attrs['href'])
##            return internalLinks
##            
###Retrieves a list of all external links found on a page
##def getExternalLinks(bsObj, excludeUrl):
##    externalLinks = []
##    #Finds all links that start with "http" or "www" that do
##    #not contain the current URL
##    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
##        if link.attrs['href'] is not None:
##            if link.attrs['href'] not in externalLinks:
##                externalLinks.append(link.attrs['href'])
##            return externalLinks
##
##def splitAddress(address):
##    addressParts = address.replace("http://", "").split("/")
##    return addressParts
##
##def getRandomExternalLink(startingPage):
##    html = urlopen(startingPage)
##    bsObj = BeautifulSoup(html)
##    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
##    if len(externalLinks) == 0:
##        internalLinks = getInternalLinks(startingPage)
##        return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
##    else:
##        return externalLinks[random.randint(0, len(externalLinks)-1)]
##    
##def followExternalOnly(startingSite):
##    externalLink = getRandomExternalLink("http://www.fidessa.com/news-and-events")
##    print("Random external link is: "+externalLink)
##    followExternalOnly(externalLink)
##
##
###Collects a list of all external URLs found on the site
##allExtLinks = set()
##allIntLinks = set()
##def getAllExternalLinks(siteUrl):
##    html = urlopen(siteUrl)
##    bsObj = BeautifulSoup(html)
##    internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
##    externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
##    for link in externalLinks:
##        if link not in allExtLinks:
##            allExtLinks.add(link)
##            print(link)
##        for link in internalLinks:
##            if link not in allIntLinks:
##                print("About to get link: "+link)
##                allIntLinks.add(link)
##                getAllExternalLinks(link)
##            
##getAllExternalLinks("http://www.fidessa.com/news-and-events")





