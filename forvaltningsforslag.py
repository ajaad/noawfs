#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys
# Importer pakker fra virtulet miljo:
sys.path.insert(0,"virtEnv/lib/python3.11/site-packages")

import os
import pywfs
        
if __name__ == "__main__":

    
    if os.environ["QUERY_STRING"]:
        wfs = pywfs.Service("Forvaltningsforslag",
                           "data/forvaltningsforslag/forvaltningsforslag.csv")
        
        # Respond to the the query
        wfs.response(os.environ["QUERY_STRING"])
        
    else:
        # If no query provided, print a website.
        # There is no need to the wfs-object if there is no query.
        
        print("Content-type: text/html; charset=UTF-8\n")
        file = open("data/forvaltningsforslag/index.html", 'r')
        content = file.read()
        file.close()
        print(content)