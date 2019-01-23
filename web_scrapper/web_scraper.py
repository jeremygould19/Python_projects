#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 21:36:19 2018

@author: jeremygould
"""
#I wrote this code as part of a PoC and only needed to scrap
#a few web pages.  It appears that the library Scrapy could also
#be used and it could likely do a more thorough job of
#of crawling through all links in a web page

import time
import requests
import os
from bs4 import BeautifulSoup

os.chdir('<file path for writing html file to>')

#add urls below that you'd like to scrap;
#backslash is used to write multi-line code
urls = ['<url1>','<url2>','<url3>',etc...]
a = 1

for i in urls:
    html_response = requests.get(i)
    page = BeautifulSoup(html_response.content,'html.parser')
    html_file_name = "html_response_page_" + str(a) + ".html"
    Html_file = open(html_file_name,"w")
    Html_file.write(str(page.prettify)) #.prettify makes the html response formatted correctly
    Html_file.close()
    a += 1
    time.sleep(2) #adding a time delay to ensure I don't overload the website
