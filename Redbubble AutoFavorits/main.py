# Setup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

PATH = "C:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.redbubble.com/")

# Info
username = ""
password = ""
print(driver.title)

time.sleep(15)
try:
    # Tar bort cookie knappen
    search = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    time.sleep(5)
except NoSuchAttributeException:
    print("Cant find cookie button to allow it")
except:
    print("No fucking cookie button")


    # Går till inloggnings fönstret
search = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div/div/header/div[1]/a[2]').click()
time.sleep(15)


time.sleep(10)
#Inputing username and password

time.sleep(5)
driver.refresh()
print("Refreshing!")
# Loggar in
search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[1]/div/div/input')
search.send_keys(username)
search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[2]/div/div/input')
search.send_keys(password)

search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/span/button').click()

try:
    # Tar bort start cookisen
    search = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    time.sleep(5)
except NoSuchAttributeException:
    print("Cant find cookie button to allow it")
except:
    print("No fucking cookie button")
time.sleep(60)
driver.refresh()
print("Refreshing!")
time.sleep(25)
driver.refresh()
print("Refreshing!")
time.sleep(15)
driver.refresh()
print("Refreshing!")

try:
    # Random popup
    if driver.find_element_by_xpath('/html/body/div[1]/div[7]/button'):
        driver.refresh()

except:
    print("No fucking random popup!")
likes = 0
while(True):
    time.sleep(1)
    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 1")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 2")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[3]/div/div[1]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 3")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[4]/div/div[1]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 4")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[5]/div/div[1]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 5")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[6]/div/div[1]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 6")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 7")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 8")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 9")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[4]/div/div[2]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 10")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[5]/div/div[2]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 11")
    time.sleep(10)

    try:
        #Click like button
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[4]/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[6]/div/div[2]/a/div/div[1]/div/button').click()
        likes = likes + 1
        print("Im working")
    except:
        print("Cant find anything to click on step 12")
    time.sleep(10)
    try:
        # Go back to start page
        search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/button/span/svg').click()
    except:
        print("Not looked")
    time.sleep(1)
    try:
        search = driver.find_element_by_class_name('node_modules--redbubble-design-system-react-Modal-ModalOverlay-styles__dismiss--1RFz2').click()
    except:
        print("Still not looked")

    time.sleep(15)
    driver.refresh()

