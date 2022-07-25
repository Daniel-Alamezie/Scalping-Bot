import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Future implementation - add a list of url and loop through each one finding different items


# Selenium portal set-up

driver = webdriver.Chrome()


# open Url
driver.get("https://www.amazon.co.uk/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.uk%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=gbflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(1)

# Get login details

def logIn():

    # Get Phone number details
    number = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
    number.send_keys("") # Enter your Phone number here
    submit = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
    submit.click()

    # Get password details
    password = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input")
    password.send_keys("") # Enter your amazon password here
    signin = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input")
    signin.click()
    time.sleep(1)


# find item

# More functions can be added for different item, see "findGPU" as code template for when more items needs to be added


def findGpu():

    # Would only find the id if the webpage has it
    driver.get("https://www.amazon.co.uk/Palit-GamingPro-Graphics-DisplayPort-lighting/dp/B096KVBBHQ/ref=sr_1_5?crid=3A30EQU199NDN&keywords=3080+ti&qid=1658331824&sprefix=3080ti%2Caps%2C86&sr=8-5")
    cartload = driver.find_element("id", "add-to-cart-button")
    time.sleep(3)
    cartload.click()
    complete = driver.find_element("xpath", "/html/body/div[4]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
    time.sleep(0.5)
    complete.click()
    time.sleep(0.5)
    driver.get("https://www.amazon.co.uk/Palit-GamingPro-Graphics-DisplayPort-lighting/dp/B096KVBBHQ/ref=sr_1_5?crid=3A30EQU199NDN&keywords=3080+ti&qid=1658331824&sprefix=3080ti%2Caps%2C86&sr=8-5")


# return to home page


def homePage():

    driver.get("https://www.amazon.co.uk/ref=nav_logo")


# refresh page


def refreshPage():

    driver.refresh()


# Function calls
logIn()
findGpu()

