# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:19:55 2014

@author: Kieran
"""

import requests
import re
import sys
import os

class ComicMiner(object):
    
    #The base url for the web comic site
    BaseUrl = ''
    
    #The first comic in the strip
    StartUrl = ''
    
    #The base storage directory
    StorageDir = './Comics/'
    
    #The comics name
    ComicName = ''
    
    #Next comic regex
    NextComicRegex = r''
    
    #Image regex
    ComicImageRegex = r''
    
    #Are the images hosted on the main site
    RelativeImages = True
    
    #Sometimes the site directs to an arbitrary url instead of not have a next link
    EndUrl = None
    
    #Data used to start the session
    StartSessionData = {}
    
    def __init__(self):
        # HTTP session storing cookies
        self.Session = requests.session()
    
    def startSession(self, url):
        self.gotoUrl(url, self.Session, self.StartSessionData)
        return url
    
    def gotoUrl(self, url, session, data = None):
        kwargs = {}
        if data is None:
            func = session.get
        else:
            kwargs['data'] = data
            func = session.post
        try:
            req = func(url, **kwargs)
            return req
        except requests.exceptions.RequestException as err:
            msg = 'URL retrieval of %s failed: %s' % (url, err)
            raise IOError(msg)
    
    def findNextUrl(self, html):
        matchObjects = re.finditer(self.NextComicRegex, html, re.I|re.M)
        nextUrl = None
        #The regex matches multiple overlapping href tags, so we need to find the smallest one which is the one we want
        if matchObjects:
            
            minLen = sys.maxsize
            for matchObject in matchObjects:
                matchedString = matchObject.group(2)
                if len (matchedString) < minLen:
                    nextUrl = matchedString
        
        if nextUrl == self.EndUrl:
            nextUrl = None
        
        return nextUrl
    
    def findComicImage(self, html):
        matchObject = re.search(self.ComicImageRegex , html, re.I|re.M)
        if not self.RelativeImages:
            return matchObject.group(1)
        return self.BaseUrl + matchObject.group(1)
    
    def downloadComicImage(self, imageUrl, prefix = "", comicDir = './Comics/ComicName'):
        r = requests.get(imageUrl, stream=True)
        imageName = prefix + imageUrl.split('/')[-1]
        if r.status_code == 200:
            if not os.path.exists(comicDir):
                os.makedirs(comicDir)
    
            localImageFile = comicDir + imageName        
            if not os.path.isfile(localImageFile):
                with open(localImageFile, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
            else:
                print ("WARNING: File {0} already exists. Skipping download.".format(localImageFile))
    
    def formatCount(self, count):
        return "0" * (4 - len(str(count))) + str(count)
        
    
    def downloadComic(self, isTest = False, maxComics = sys.maxsize):
        self.startSession(self.BaseUrl)
        count = 0
        nextUrl = self.StartUrl
        while nextUrl and count < maxComics:
            htmlResponse = self.gotoUrl(self.BaseUrl + nextUrl, self.Session)
            currentImageUrl = self.findComicImage(htmlResponse.text) 
            print ("Current Image Url: {0}".format(currentImageUrl))
            if not isTest:
                self.downloadComicImage(currentImageUrl, self.formatCount(count) + "-", self.StorageDir + self.ComicName + "/")
            nextUrl = self.findNextUrl(htmlResponse.text)
            print ("Next Url: {0}".format(nextUrl))
            count += 1