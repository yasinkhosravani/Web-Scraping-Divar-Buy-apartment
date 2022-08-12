#!/usr/bin/env python
# coding: utf-8

# In[348]:

from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import requests



page = requests.get("https://divar.ir/s/shiraz/real-estate")
soup = bs(page.content)
x=str(soup.find_all(class_='kt-post-card__title'))
x=x.replace('</h2>',' ').replace('<h2 class="kt-post-card__title">',' ')
x=x.split(", ")
z=len(x)


def title(l):
    x=str(soup.find_all(class_='kt-post-card__title'))
    x=x.replace('</h2>',' ').replace('<h2 class="kt-post-card__title">',' ')
    x=x.split(", ")
    z=len(x)
    return x[l]
def price(l):      
    x=str(soup.find_all(class_='kt-post-card__description'))
    x=x.replace('</div>',' ').replace('<div class="kt-post-card__description">',' ')
    x=x.split(", ")        
    return x[l]


for i in range(0 ,z):
    print(title(i),price(i))           



