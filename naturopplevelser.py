#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys
# Importer pakker fra virtulet miljo:
sys.path.insert(0,"virtEnv/lib/python3.11/site-packages")

import os
import pywfs

try:
    query_string = os.environ["QUERY_STRING"]
except:
    query_string = "request=getxmlinfo"
        
if __name__ == "__main__":

    
    if query_string:
        wfs = pywfs.Service("Naturopplevelser",
                           "data/naturopplevelser/naturopplevelser.csv")
        
        # Respond to the the query
        wfs.response(query_string)
        
    else:
        # If no query provided, print a website.
        # There is no need to the wfs-object if there is no query.
        
        print("Content-type: text/html; charset=UTF-8\n")
        file = open("data/naturopplevelser/index.html", 'r')
        content = file.read()
        file.close()
        print(content)