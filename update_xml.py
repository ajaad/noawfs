#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# This script creates the .xml-file
# which was supposed to be created by index.py.
# That did not work because the browsers didn't wait for
# the url requests.

import bs4
import requests
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    
    query_string = "request=getxmlinfo"
    urlroot = "https://markakartet.localhost/wfs/"
    
    wfs_dict  = {"Naturopplevelser": "naturopplevelser.py",
                 "Verneforslag": "verneforslag.py",
                 "Forvaltningsforslag": "forvaltningsforslag.py"}
    
    # Create file
    xml = open("service.xml", "w")
    
    # 
    soup = bs4.BeautifulSoup()
    main = soup.new_tag("main")
        
        
    for wfs_name in wfs_dict.keys():
                
        # Call service for layers 
        url = urlroot + wfs_dict[wfs_name] + "?REQUEST=GetXMLinfo"
        r = requests.get(url, verify=False)
                
        service =  bs4.BeautifulSoup(r.content, features="html.parser")
        main.append(service)
                
        soup.append(main)
        
    xml.write(str(soup))
    xml.close()