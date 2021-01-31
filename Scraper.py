# -*- coding: utf-8 -*-
"""

@author: barengific
"""

import requests as req
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

res = req.get(url)

soup = BeautifulSoup(res.text,'lxml')
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a',class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)
        
        
        
url = 'https://scrapingclub.com/exercise/list_basic/'
count = 1
response = req.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('a', class_='page-link')
urls = []
for page in pages:
    pageNum = int(page.text) if page.text.isdigit() else None
    if pageNum != None:
        link = page.get('href')
        urls.append(link)
for i in urls:
    response = req.get(url + i)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1