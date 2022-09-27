# Python 🐍 Dinner Menu Generator 🍗🥞🥙🍕

View and run this code on Replit - https://replit.com/@PythonWrangler/dinnerparty?v=1

Note - Browser opening function not available on replit

*Day 10 of 100 days of code*

### Description:
This is a python app that uses scraped data from Olivemagazine.com to randomly generate a 3 course dinner menu. 
This app was create to try and help my girlfirend and I try new dishes when we entertain guests instead of cooking the same 
meals over and over. 

The app uses data that was scraped using the scrape.py file. The scrape file scrapes a recipes name as well as its URL and stores these in three 
files for starters, mains and desserts. Using the os module the scrape.py file stores all of these in a folder call menu menu_files. 

app.py reads in these files and saves the dish name and link as a list of tuples. 
Using the random module a random dish from each list is selected. 
This is then displayed to the user, with the options to either:
- Open the recipe links in their browser
- Swap out a menu item
- Generate a new menu
- Exit the app

### What I learnt:
- writing and reading to text files 📁
- using bs4 and basic webscraping 🕸️
- using random.choice() instead of generating random integers to index a list at random 🎲
