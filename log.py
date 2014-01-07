# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:05:00 2014

Small logging script

@author: Kieran Bristow
"""
info_prefix = "INFO: "
warning_prefix = "WARNING: "
error_prefix = "ERROR: "
debug_prefix = "DEBUG: "

def info (msg):
    log (info_prefix + msg)

def warning (msg):
    log (warning_prefix + msg)

def error (msg):
    log (error_prefix + msg)
    
def debug (msg):
    log (debug_prefix + msg)
    
def log (msg):
    print (msg)