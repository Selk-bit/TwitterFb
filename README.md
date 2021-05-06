A python-scripted web scraper using the Selenium module and chromedriver.

The script accesses a Twitter account and scrapes the first six tweets (you can configure this to whatever you want but make sure to add more scrolls in case you increased the number of tweets to scrape), to check afterwards whether or not one of them contains a certain word. If so, then the script logs in to your Messenger account using the fbchat module that interacts with Facebook, to notify you by sending a certain message.

all the personal data needed to be filled such as Facebook email and password, and Twitter account to scrape, are marked in the source code.
you can run ***pip install requirements.txt*** to install all modules needed to run this script.

make sure to add chromedriver to the PATH variables or reference its relative/absolute path inside the ***chrome()*** method as shown in the code.

Have a Nice Day.
