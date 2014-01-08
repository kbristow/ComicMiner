# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:34:07 2014

Stores configurations of the ComicMiner object for specific web comics.

@author: Kieran Bristow
"""

from comic_miner import ComicMiner 

#NOTE TO SELF: Get better at regex's

class Dorkly(ComicMiner):
    #The app works very poorly for this comic strip because it uses an odd format

    #The base url for the PDL website
    BaseUrl = 'http://www.dorkly.com/'    
    
    #Not actually the first comic but something weird happens with the ones before this.
    StartUrl = 'comic/10575/dueling-analogs-stroke-of-genius'
    
    #The comics name
    ComicName = 'Dorkly'
    
    #Next comic regex
    NextComicRegex = r'(?=(<a href="/((comic)?(article)?/.*?)".*?title="Previous article"))'
    
    #Image regex
    ComicImageRegex = r'"og:image" content="(.*?)">'
    
    #Dorkly has full link to the image
    RelativeImages = False
    

class LoldWell(ComicMiner):
    #The base url for the PDL website
    BaseUrl = 'http://loldwell.com/'    
    
    #First Comic
    StartUrl = '?comic=stick-figures'
    
    #The comics name
    ComicName = 'LoldWell'
    
    #Next comic regex
    NextComicRegex = r'(?=(rel="next" href="http://loldwell.com/(\?comic=.*?)"))'
    
    #Image regex
    ComicImageRegex = r'"og:description".*?\n.*?"og:image" content="(.*?)"'
    
    #LoldWell has full link to the image
    RelativeImages = False
    

class Oglaf(ComicMiner): 
    #The base url for the oglaf website
    BaseUrl = 'http://oglaf.com/'
    
    #The first oglaf comic
    StartUrl = 'cumsprite/'
    
    #The comics name
    ComicName = 'Oglaf'
    
    #Next comic regex
    NextComicRegex = r'(?=(<a href="/(.*?)"><div id="nx" class="nav_ro">))'
    
    #Image regex
    ComicImageRegex = r'<img id="strip" src="(.*?)".*?'
    
    # click the "I am 18" button
    StartSessionData = {"over18": "&nbsp;"}
    
    #Oglaf hosts images somewhere else
    RelativeImages = False
    
class OrderOfTheStick(ComicMiner):
    #The base url for the oglaf website
    BaseUrl = 'http://www.giantitp.com/'
    
    #The first oglaf comic
    StartUrl = 'comics/oots0001.html'
    
    #The comics name
    ComicName = 'OrderOfTheStick'
    
    #Next comic regex
    NextComicRegex = r'(?=(<A href="/?(.*?)"><IMG.*?alt="Next Comic"))'
    
    #Image regex
    ComicImageRegex = r'<TD align="center"><IMG src="/(comics/images/.*?)"></TD>'
    
    #OOTS directs to a # at the latest comic
    EndUrl = "#"

class PoorlyDrawnLines(ComicMiner):
    #The base url for the PDL website
    BaseUrl = 'http://poorlydrawnlines.com/'
    
    #The first PDL comic
    StartUrl = 'comic/campus-characters/'
    
    #The comics name
    ComicName = 'PoorlyDrawnLines'
    
    #Next comic regex
    NextComicRegex = r'(?=("http://poorlydrawnlines\.com/(comic/.*?)" rel="next">))'
    
    #Image regex
    ComicImageRegex = r'src="(http://poorlydrawnlines\.com/wp-content/uploads/.*?)"'
    
    #PDL has full link to the image
    RelativeImages = False

class SMBC(ComicMiner):
    #The base url for the SMBC website
    BaseUrl = 'http://www.smbc-comics.com/'
    
    #The first SMBC comic
    StartUrl = '?id=1#comic'
    
    #The comics name
    ComicName = 'SMBC'
    
    #Next comic regex
    NextComicRegex = r'(?=(<a href="(\?id=.*?#comic)" title="" class="nextRollover"></a>))'

    #Image regex
    ComicImageRegex = r'<img src=\'(http://www\.smbc-comics\.com/comics/.*?)\'>'
    
    #SMBC hosts images on its site but provides the full url
    RelativeImages = False
    
class XKCD(ComicMiner):
    #The base url for the SMBC website
    BaseUrl = 'http://xkcd.com/'
    
    #The first SMBC comic
    StartUrl = '1/'
    
    #The comics name
    ComicName = 'XKCD'
    
    #Next comic regex
    NextComicRegex = r'(?=(rel="next" href="/(.*?)"))'

    #Image regex
    ComicImageRegex = r'<img src="(http://imgs\.xkcd\.com/comics/.*?)"'
    
    #XKCD hosts images on another site
    RelativeImages = False