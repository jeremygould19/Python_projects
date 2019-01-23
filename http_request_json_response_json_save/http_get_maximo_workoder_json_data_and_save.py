#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 21:18:10 2018

@author: jeremygould
"""

### the below code sent an HTTP GET request to a web server and saved the
### json document response in a file in my local file system.  However, at
### first I was getting a 406 error code as a response, which appeared to
### mean that my code wasn't set up to accept json as a response.  I played
### around with the headers by adding the 'accept' and 'content-type' headers
### and the response started working.  I have the lines commented out in the code
### below because when I tried to start commenting out the headers I added to
### figure out what worked, the request started working with out needing the headers
### at all.

import requests
import json
import os

url='<url>'
### the below lines appeared to help work through an issue with getting a 406 response error from the http
### server; but it was difficult to tell what actually got this to work ultimately
#headers = {'Accept': 'application/json','Content-Type':'application/json'}
#r = requests.get(url, headers = headers)
r = requests.get(url)
json_data = r.json()

os.chdir('<intended file path for the next json docuement>')

with open('worder_order.json', 'w') as outfile:
    json.dump(json_data, outfile, ensure_ascii=False)
