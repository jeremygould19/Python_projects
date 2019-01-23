#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 08:17:19 2018

@author: jeremygould
"""

import requests
import os
import json
import csv

headers = {}

headers['APIKEY'] = <api key>
headers['Content_type'] = 'multipart/form-data'
filePath = <insert file path>

url = '<url>'

output_file_and_path =<insert file path plus intended file name and extension>

def score_files():
    file_scores_Master_list = []
    for i in os.listdir(filePath):
        print(i)
        path = filePath + "/" + i
        files = {'data':open(path,'rb')}
        score = requests.post(url, headers=headers, files=files)
        ai_response = (score.text)
        ai_dict_resp = json.loads(ai_response)
        print(ai_dict_resp)
        return ai_dict_resp
