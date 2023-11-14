# step 0:
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# 1st Web 24hours.pk DataFrame:
baseurl = "https://24hours.pk/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
productlinks = []
for x in range(1,3):
    r = requests.get(f"https://24hours.pk/collections/electronics?page={x}")
    soup = BeautifulSoup(r.content, 'html.parser')
    # Call all div:
    productlist = soup.find_all('div', class_='grid-item small--one-half medium--one-quarter large--one-quarter')
    #print(productlist)
    # CAll all anchors tags present in div:
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
#print(productlinks)

# Get information for individual product:
# testlink = 'https://24hours.pk/collections/electronics/products/pack-of-12-flameless-led-tea-light-candles-random-colors'
electronic_list = []
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    name = soup.find('h1',class_='h2').text.strip()
    actual_price = soup.find('span',class_='visually-hidden').text.strip()
    electronic = { # make a dictionary
        'name':name,
    '   actual_price':actual_price
}
    electronic_list.append(electronic)
    #print(electronic)
df = pd.DataFrame(electronic_list)
#print(df.head(12))

# 2nd Web ishopping.pk Data Frame :
baseurl_1 = "https://www.ishopping.pk/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
productlinks_1 = []
for x in range(1,2):
    r1 = requests.get(f'https://www.ishopping.pk/catalogsearch/result/index/?p={x}&q=NINTENDO')
    soup_1 = BeautifulSoup(r1.content, 'html.parser')
    productlist_1 = soup_1.find_all('div', class_='product-item-details')
    #print(productlinks_1)
    for item in productlist_1:
        for link_1 in item.find_all('a',href=True):
            productlinks_1.append(link_1['href'])
#print(len(productlinks_1))

# Get information for individual product:
#testlink_1 = 'https://www.ishopping.pk/nintendo-switch-lite-console-coral-price-in-pakistan.html'
gaming_list=[]
for link_1 in productlinks_1:
    r1 = requests.get(link_1,headers=headers)
    soup_1 = BeautifulSoup(r1.content,'html.parser')
    name_1 = soup_1.find('div',class_='title-area').text.strip()
    price = soup_1.find('span',class_='price').text.strip()
    gaming = {
        'name_1':name_1,
        'price':price
}
    gaming_list.append(gaming)
    #print(gaming['name_1'])

gf = pd.DataFrame(gaming_list)
print(gf.head())
# Comparison of two data frames:
print(df.compare(gf,keep_equal=True,keep_shape=True))