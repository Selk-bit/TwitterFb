import time
import os
import fbchat
from fbchat import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException        


browser = webdriver.Chrome('./chromedriver')



twitter_username = "<Twitter Account>"
browser.get("https://twitter.com/" + twitter_username)

def check_exists_by_xpath(xpath):
    try:
	    browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

time.sleep(15)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 2

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

isExisting = 'Does not Exist'


for x in range(6):
	if check_exists_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div['+ str(x) +']/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span') == True :
		recent_tweet = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div['+ str(x) +']/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span')
	if 'recent_tweet' in locals():
		print(recent_tweet.text)
		if recent_tweet.text.find("Ramadan") >= 0:
			isExisting = 'it does Exist'

	for y in range(1, 6):
		if check_exists_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div['+ str(x) +']/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span['+ str(y) +']') == True :
			add = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div['+ str(x) +']/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span['+ str(y) +']')
		if 'add' in locals():
			print("------------>" + add.text)
			if add.text.find("Ramadan") >= 0:
				isExisting = 'it does Exist'

print(isExisting)



browser.quit()

if isExisting=="it does Exist":
	print("entered")
	client = fbchat.Client(<here put your email>, <here put your password>)
	send = client.send(fbchat.models.Message("<Your Message>"), <Rceiver Facebook Id>)
	if send:
		print("Success")