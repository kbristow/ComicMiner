# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:13:07 2014

Used to convert images to a specific file type since some formats like gif are
not great for standard viewing on windows. Uses python Pillow package.

@author: Kieran Bristow
"""
import glob
import log
from PIL import Image

def convertImage(sourceFile, newExtension):
    try:
        outputFile = sourceFile[:sourceFile.rfind(".")] + "." + newExtension
        im = Image.open(sourceFile)
        newImage = Image.new('RGB', im.size, (255,255,255))
        newImage.paste(im)
        newImage.save(outputFile)
    except IOError:
        log.error("Cannot convert", sourceFile)

ootsGlob = "./Comics/OrderOfTheStick/*.gif"
smbcGlob = "./Comics/SMBC/*.gif"

for sourceFile in glob.glob(smbcGlob):
    convertImage(sourceFile, "jpg")