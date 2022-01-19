#import csv
import time
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.ui import WebDriverWait

# I use Chrome and Chromedriver, feel free to change to any browser of your choice below.

PATH = "filepath/chromedriver.exe" # add Chromedriver file path here.
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10)
form_url = "https://twitter.com/username" # add specific username or url of tweets here.

def scrape_tweets():

    driver.get(form_url)
    time.sleep(3)
    elem = driver.find_element(By.TAG_NAME, "body")

    pagedowns = 0 # Choose the amount of times you want to scroll down the feed.

    for x in range(pagedowns):
        previous_height = 0

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # If your pagedowns is a high number, consider adding more sleep time below to avoid crashing.
        time.sleep(5)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == previous_height:
            break

        previous_height = new_height

        tweets = elem.find_elements(By.TAG_NAME, "article")
        
        # Copy files to a tweets.txt file - add filepath below.
        with open('filepath/tweets.txt', 'a+') as file:
            for tweet in tweets:
                data = tweet.text.split('\n')
                file.write(data[4])
                file.write('\n')

scrape_tweets()