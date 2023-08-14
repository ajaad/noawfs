#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import bs4

import requests
requests.packages.urllib3.disable_warnings()

# This is a superservice script

# It provides an list of available WFS-services within the service.

# List the WFS-services that should be available:
    
wfs_dict  = {"Naturopplevelser": "naturopplevelser.py",
             "Verneforslag": "verneforslag.py",
             "Forvaltningsforslag": "forvaltningsforslag.py"}

if __name__ == "__main__":

    try:
        query_string = os.environ["QUERY_STRING"]
        urlroot = os.environ["REQUEST_SCHEME"] + "://" + os.environ["HTTP_HOST"] + os.environ["CONTEXT_PREFIX"] + "/"  
        #print("Content-type: text/html; charset=UTF-8\n")
        #print(os.environ)
        
        # os.environ["REQUEST_URI"] 
        
        #print(urlroot)
    except:
        # To be able to test the script in a terminal.
        query_string = "request=getxmlinfo"
        urlroot = "https://markakartet.localhost/wfs/"
        
    if query_string:
        # Create a list to be used for applications
        # it shall contain information such as
        # layer, color of layer, description and abstract.
        
        
        # Please update the .xml-file if not updated.
        
        file = open("service.xml", 'r')
        content = file.read()
        file.close()
        
        
        print("Content-type: text/xml; charset=UTF-8\n")
        print(content)

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
        
        
        