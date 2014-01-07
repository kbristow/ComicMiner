# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 23:13:34 2014

@author: Kieran Bristow
"""

from configurations import Oglaf, OrderOfTheStick, SMBC, XKCD

#oglafMiner = Oglaf()
#oglafMiner.downloadComic(isTest = True, maxComics = 10)

ootsMiner = OrderOfTheStick()
ootsMiner.downloadComic(isTest = False, maxComics = 10)

smbcMiner = SMBC()
smbcMiner.downloadComic(isTest = False, maxComics = 10)

xkcdMiner = XKCD()
xkcdMiner.downloadComic(isTest = False, maxComics = 10)