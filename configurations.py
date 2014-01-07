# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:34:07 2014

Stores configurations of the ComicMiner object for specific web comics.

@author: Kieran Bristow
"""

from comic_miner import ComicMiner 

#NOTE TO SELF: Get better at regex's

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
    ComicImageRegex = r'<img src=\'(http://www.smbc-comics.com/comics/.*?)\'>'
    
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
    ComicImageRegex = r'<img src="(http://imgs.xkcd.com/comics/.*?)"'
    
    #XKCD hosts images on another site
    RelativeImages = False