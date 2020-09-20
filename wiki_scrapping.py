#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 22:48:51 2019

@author: KERKEB Yasmina
"""
import time
from urllib.request import urlopen
from urllib.parse import urljoin 
from lxml.html import fromstring
from nltk.tokenize import sent_tokenize
import xlrd
import json
from bs4 import BeautifulSoup as bs
import re
from time import sleep
import sys
import logging

########## Parameters ###################

search_url="https://en.wikipedia.org/w/index.php?search={}&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%22namespaces%22%3A%5B0%5D%7D&ns0=1"
keywords_filename="keywords.xlsx"
start=time.time()
# regex pattern  to check for numbers
digit_pattern=re.compile(r'[(^\d)*]\d+')
# Get the main content of a page
main_pattern=re.compile(r'<(p|table)((.|\n)*?)\<h2\>')

#Initialize a dictionary to load links for each keyword
keyword_links={}

#Logging file
log_filename="log_file.log"

########## Loading the keywords ######################

doc=xlrd.open_workbook('keywords.xlsx').sheet_by_index(0)
keywords=doc.col_values(0,0,50)

#########Creating the log file ########################
logging.basicConfig(filename='log_file.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

########## Main code ##########################
for i, word in enumerate(keywords[:20]):
    #Keep track of the progress
    logging.info(f"keyword {i}:{word}")
    #Search the url with the right keyword
    response = urlopen(search_url.format(word)).read().decode("utf-8")
    #Use Beautiful Soup to parse the content
    parsed_html=bs(response, "html.parser")
    parsed_links=parsed_html.find_all("a",{"data-serp-pos":re.compile('^[0-9]$')}) 
    links=list(map(lambda x:x.get('href'),parsed_links))
    keyword_links[word]=links
    for link in links:
        url=urljoin("https://en.wikipedia.org",link)
        response=urlopen(url.format(word)).read().decode("utf-8")
        #We are only interested in the main part of the page
        body=main_pattern.search(response).group()
        #Use Beautiful Soup to parse the content
        body=bs(body,"html.parser")
        #Remove irrelevant tags instances 
        to_remove=body.find_all(['script','style','table','span'])
        for string in to_remove:
            string.extract()
        #Get text
        main_content=body.text
        #Remove references
        main_content=re.sub(r'(\[(.|\n)*\]|\n(\s)+)','',main_content)
        #Extract all sentences
        sentences = sent_tokenize(main_content)
        #Keep only sentences with digits
        with open('content.txt','a') as f:
            f.write(f"### {word} - {link} \n\n")
            for element in sentences:
                if digit_pattern.search(element):
                    f.write(f'- {element} \n')
            f.write("\n\n")
            
f.close()

# Export results in json
with open('search_urls.json','w') as f:
    json.dump(keyword_links,f)
f.close()
logging.info("Export done")
end=time.time()
duration=end-start
logging.info(f'Time Indicator={duration} s')


        
        


