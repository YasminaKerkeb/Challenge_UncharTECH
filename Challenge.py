#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:23:06 2019

@author: mac
"""

#Packages imported
from urllib.request import urlopen
import time
from nltk.tokenize import sent_tokenize
from lxml.html import fromstring
import xlrd
import re


#Load the keywords
tp1=time.time()
doc = xlrd.open_workbook('keywords.xlsx').sheet_by_index(0)
keywords=doc.col_values(0,0,50);

#Reaching the wikipedia page


#Searching the words
for i, x in enumerate(keywords):
    print("keyword :",i, x)
    response = urlopen('https://en.wikipedia.org/w/index.php?search='+x+'&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%22namespaces%22%3A%5B0%5D%7D&ns0=1')
    html = response.read()
    html=html.decode("utf-8")
    #Searching the first 10 results
    links=re.findall(r'<a href=[\'"]?([^\'" >]+)"\stitle=[^>]*\sdata-serp-pos="[0-9]">',html)
    with open(x+'.txt', 'a', encoding='utf-8') as f:
        f.write('****************'+'\n')
        f.write(x+'\n')
        f.write('****************'+'\n')
        
        for y in links:
            search=urlopen('https://en.wikipedia.org'+y);
            page=search.read()
            page=page.decode("utf-8");
            pattern=re.compile(r'<p>((.|\n)*?)\<h2\>') #We are only interested in the main part of the page
            body=pattern.search(page) # return the relevant data
            body=body.group()
            #Let's clean a bit this data and keep the main content solely consisted of sentences
            body=re.sub(r'<script*>*</script>','',body)
            body=re.sub(r'<style (.|\n)*?\<\/style>','',body)
            body=re.sub(r'<span (.|\n)*?\<\/span>','',body)
            body=re.sub(r'<table (.|\n)*?\<\/table\>','',body) #Removing the table infos on the side
            body=re.sub(r'<sup (.|\n)*?\<\/sup>','',body) #Removing the reference digits
            pageElement = fromstring(body) #Extracting the text inside the HTML tags
            textContent = str(pageElement.text_content())
            sentences = sent_tokenize(textContent)
            #Extracting the sentences with numbers and
            #Writing the relevant sentences on the file   
            pattern=re.compile(r'(\d)+')
            f.write('##############'+'\n')
            f.write(''.join([y[6:len(y)]])+'\n')
            f.write('##############'+'\n')
            for z in sentences:
                if re.search(pattern,z) :
                    f.write(z)
        
            f.write('\n')
            
    f.close()



    
                
tp2=time.time()
print('Time Indicator=',tp2-tp1)




