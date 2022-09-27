#########################################
# Python Scraper for Menu Items
#########################################

# import necessary libraries
from bs4 import BeautifulSoup
import requests
import os

# get info for the starters web page
page = requests.get(
    "https://www.olivemagazine.com/recipes/entertain/best-ever-starter-recipes/")

soup = BeautifulSoup(page.content, 'html.parser')

# get info for the mains web page
page_mains = requests.get(
    'https://www.olivemagazine.com/recipes/collection/best-ever-easy-52-recipes-under-500-calories/')
page_mains_2 = requests.get('https://www.olivemagazine.com/recipes/collection/best-ever-family-friendly-recipes/')
page_mains_3 = requests.get('https://www.olivemagazine.com/recipes/collection/best-ever-dinner-party-mains/')

soup_mains = BeautifulSoup(page_mains.content, 'html.parser')
soup_mains_2 = BeautifulSoup(page_mains_2.content, 'html.parser')
soup_mains_3 = BeautifulSoup(page_mains_3.content, 'html.parser')

# get info for the desserts mains
page_desserts = requests.get(
    'https://www.olivemagazine.com/recipes/baking-and-desserts/best-spanish-dessert-recipes/')

soup_desserts = BeautifulSoup(page_desserts.content, 'html.parser')

page_desserts_2 = requests.get(
    'https://www.olivemagazine.com/recipes/baking-and-desserts/best-british-dessert-recipes/')

soup_desserts_2 = BeautifulSoup(page_desserts_2.content, 'html.parser')

# initialise empty lists
# loop through BeautifulSoup objects
# store tuples of dish name and link in lists

starters = []
mains = []
desserts = []

for i in soup.find_all('h3')[1:-3]:
    a_tag = i.find_all("a")

    for i in a_tag:
        link = i.attrs['href']
        title = i.text

        starters.append((title, link))

for i in soup_mains.find_all('h3'):
    a_tag = i.find_all("a")

    for i in a_tag:
        link = i.attrs['href']
        title = i.text

        mains.append((title, link))
        
for i in soup_mains_2.find_all('h3'):
    a_tag = i.find_all("a")

    for i in a_tag:
        link = i.attrs['href']
        title = i.text

        mains.append((title, link))
        
for i in soup_mains_3.find_all('h3'):
    a_tag = i.find_all("a")

    for i in a_tag:
        link = i.attrs['href']
        title = i.text

        mains.append((title, link))

for i in soup_desserts.find_all('h3'):
    a_tag = i.find_all("a")

    for i in a_tag:
        link = i.attrs['href']
        title = i.text

        desserts.append((title, link))

for i in soup_desserts_2.find_all('h3'):
    a_tag = i.find_all("a")

    for i in a_tag:
        link = i.attrs['href']
        title = i.text

        desserts.append((title, link))

# create folder menu items
#write lists to file to read into app.py

os.mkdir(".\menu_files")

sfile = open('.\menu_files\starters.txt', 'w')
mfile = open('.\menu_files\mains.txt', 'w')
dfile = open('.\menu_files\desserts.txt', 'w')

menu_files = [sfile, mfile, dfile]

for starter in starters:
    name = starter[0]
    link = starter[1]

    sfile.write(f'{name},{link}\n')

for main in mains:
    name = main[0]
    link = main[1]

    mfile.write(f'{name},{link}\n')

for dessert in desserts:
    name = dessert[0]
    link = dessert[1]

    dfile.write(f'{name},{link}\n')

# close files
for file in menu_files:
    file.close()
