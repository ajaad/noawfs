#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys
# Importer pakker fra virtulet miljo:
#sys.path.insert(0,"/var/www/markakartet/wfs2/virtEnv_noa/lib/python3.11/site-packages")
sys.path.insert(0,"virtEnv/lib/python3.11/site-packages")

import os
import pywfs
        
if __name__ == "__main__":

    
    if os.environ["QUERY_STRING"]:
    	  
        # Create a WFS-service object
        # This object is created every thine one queries the service.    
        wfs = pywfs.Service("Verneforslag",
                           "data/verneforslag/verneforslag.csv")
        
        # Respond to the the query
        wfs.response(os.environ["QUERY_STRING"])
        
    else:
        # If no query provided, print a website.
        # There is no need to the wfs-object if there is no query.
        
        print("Content-type: text/html; charset=UTF-8\n")
        file = open("data/verneforslag/index.html", 'r')
        content = file.read()
        file.close()
        print(content)
        
