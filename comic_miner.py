# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:19:55 2014

Contains the base class ComicMiner used to download comics. The class is mostly driven by the downloadComic function

@author: Kieran Bristow
"""

import requests
import re
import sys
import os
import log

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
        """Starts a session using requests package.
        :param url: The main url of the web strip web page
        """
        self.gotoUrl(url, self.Session, self.StartSessionData)
        return url
    
    def gotoUrl(self, url, session, data = None):
        """Opens a url using the specified requests session. Based on the openurl function in the dosage application (https://github.com/wummel/dosage)
        :param url: The url to open
        :param session: The requests session to use to open the url
        :param data: If data is specified then a POST command is used. Otherwise a GET command is used
        """
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
            log.error(msg)
            return None
    
    def findNextUrl(self, html):
        """Finds the url for the next comic in the strip to download in an html document.
        :param html: The html code to search for the html
        """
        #Use the NextComicRegex to search the html
        matchObjects = re.finditer(self.NextComicRegex, html, re.I|re.M)
        nextUrl = None
        
        #The regex may match multiple overlapping href tags, so we need to find the smallest one which is the one we want
        if matchObjects:
            minLen = sys.maxsize
            for matchObject in matchObjects:
                matchedString = matchObject.group(2)
                if len (matchedString) < minLen:
                    nextUrl = matchedString
        
        #If the url found is the end of the line url for the comic strip we have reached the end of the strip
        if nextUrl == self.EndUrl:
            nextUrl = None
        
        return nextUrl
    
    def findComicImage(self, html):
        """Find the url for the actual comic image on a page from the html code.
        :param html: The html to search through
        """
        #Search for the url in the html using the ComicImageRegex
        matchObject = re.search(self.ComicImageRegex , html, re.I|re.M)
        
        #Decide whether it is the full url or a relative url that was found
        if not self.RelativeImages:
            return matchObject.group(1)
        return self.BaseUrl + matchObject.group(1)
    
    def downloadComicImage(self, imageUrl, prefix = "", comicDir = './Comics/ComicName'):
        """Download the image at the specified url to a local directory.
        :param imageUrl: The url for the image
        :param prefix: The prefix used when saving the file to the local directory
        :param comicDir: The local directory to save the image to
        """
        #Open a stream to the image
        r = requests.get(imageUrl, stream=True)

        imageName = prefix + imageUrl.split('/')[-1]
        
        #Check if the stream was opened successfully 
        if r.status_code == 200:
            #Create the local directory if it does not exist
            if not os.path.exists(comicDir):
                os.makedirs(comicDir)
            
            localImageFile = comicDir + imageName 
            #Skip the file if it already exists
            if not os.path.isfile(localImageFile):
                #Write the chunks of the image data from the stream to the local file
                with open(localImageFile, 'wb') as newImage:
                    for chunk in r.iter_content(1024):
                        newImage.write(chunk)
            else:
                log.warning("File {0} already exists. Skipping download.".format(localImageFile))
    
    def formatCount(self, count):
        """Formats an integer to have at least 4 digits by creating a string with 0's in front of the number. 
        :param count: The integer to format
        """
        #Chose 4 as the length somewhat arbitrarily so if it is longer just return the stringified integer
        if len(str(count)) > 4:
            return str(count)
            
        return "0" * (4 - len(str(count))) + str(count)
        
    
    def downloadComic(self, isTest = False, maxComics = sys.maxsize):
        """Download the comic strip.
        :param isTest: Used to test that the ComicMiner is correctly finding the images and next urls without downloading any images
        :param maxComix: Also used mostly in testing to limit the number of comics to go through before stopping
        """
        #Start the requests session
        self.startSession(self.BaseUrl)
        #Count is used in the naming of the local image files and to prematurely stop the comic downloads
        count = 0
        #The first url to use is the first comic in the strips URL
        nextUrl = self.StartUrl
        while nextUrl and count < maxComics:
            #Get the html from the nextUrl
            htmlResponse = self.gotoUrl(self.BaseUrl + nextUrl, self.Session)
            
            #Break if the html request fails
            if not htmlResponse:
                break
            #Find the image url in the html
            currentImageUrl = self.findComicImage(htmlResponse.text)
            log.info ("Current Image Url: {0}".format(currentImageUrl))
            if not isTest:
                #Download the comic image from the image url
                self.downloadComicImage(currentImageUrl, self.formatCount(count) + "-", self.StorageDir + self.ComicName + "/")
            
            #Find the next url in the html
            nextUrl = self.findNextUrl(htmlResponse.text)
            log.info ("Next Url: {0}".format(nextUrl))
            count += 1