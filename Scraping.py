#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.bbc.com/hindi/india-47088054"
web_page = urlopen(url)

soup = BeautifulSoup(web_page, 'html.parser')

        
for paragraph in soup.findAll("p"):
        print (paragraph.text)