#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys
# Importer pakker fra virtulet miljo:
sys.path.insert(0,"/var/www/markakartet/wfs2/virtEnv_noa/lib/python3.11/site-packages")

import os
import bs4
import pywfs

# This is a superservice script

# It provides an list of available WFS-services within the service.

wfs_dict  = {"Naturopplevelser": "naturopplevelser.py",
             "Verneforslag": "verneforslag.py",
             "Forvaltningsforslag": "forvaltningsforslag.py"}

if __name__ == "__main__":
    
    #if True:
    if os.environ["QUERY_STRING"]:
        # Create a list to be used for applications
        # it shall contain information such as
        # layer, color of layer, description and abstract.
        
        #pass
        print("Content-type: text/xml; charset=UTF-8\n")
        
        # Show layers
        soup = bs4.BeautifulSoup()
        main = soup.new_tag("main")
        
        for wfs_name in wfs_dict.keys():
            tag = soup.new_tag("service")
            tag["name"] = wfs_name
            
            # Call service for layers 
            #tag.new_tag = pywfs.getLayersInfo(wfs_dict[wfs_name])
            
            main.append(tag)
            
        soup.append(main)
            
        print(soup)
        
    else:
        
        # If no query provided,
        # return a website with a list of available services.
    
        print("Content-type: text/html; charset=UTF-8\n")
        file = open("data/main.html", 'r')
        content = file.read()
        
        soup = bs4.BeautifulSoup(content, 'html.parser')
        
        # Input the available layers to the list
        html_list = soup.find('ul', class_='wfs-list')
        for wfs_name in wfs_dict.keys():
            element = soup.new_tag("li") #, href=wfs_dict[wfs_name])
            text = soup.new_tag("a", href=wfs_dict[wfs_name] )
            text.string = wfs_name
            element.append(text)
            html_list.append(element)
            
        
        
        
        file.close()
        print(soup)
        
        
        