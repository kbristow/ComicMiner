# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 23:13:34 2014

Drives the use of the application. Currently uses a very basic menu system

@author: Kieran Bristow
"""

import inspect
import log
import configurations as configs

#All this information is used for debugging
isDebug = False
isTest = False
maxComics = 10

def getListOfComics():
    """Gets the list of available comics in the package
    """
    comicDict = {}
    for name,obj in inspect.getmembers(configs):
        if inspect.isclass(obj) and issubclass(obj, configs.ComicMiner) and name != 'ComicMiner':
            comicDict[name] = obj            
    return comicDict

def doMenuChoice():
    """Print the menu and get the choice of the user
    """
    choice = input("Enter the name of a comic to download (-l lists available comics; -x quits): ")  
    return choice

def interpretChoice(choice, comics):
    """Interpret the users choice
    :param choice: The users choice
    :param comics: A dictionary of ComicMiners available in form name:type
    """
    if choice == "-l":
        for comic in comics:
            log.log(comic)
    elif choice in comics:
        miner = comics[choice]()
        if isDebug:
            miner.downloadComic(isTest = isTest, maxComics = maxComics)
        else:
            miner.downloadComic()

def runMenu ():
    """Runs a basic menu to allow the package to be used
    """
    comicMiners = getListOfComics()
    choice = doMenuChoice()
    while not choice == "-x":
        interpretChoice(choice,comicMiners)
        choice = doMenuChoice()
    
if __name__ == "__main__":
    runMenu()
