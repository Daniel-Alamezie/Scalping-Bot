import time
from selenium import webdriver


# Selenium portal set-up
driver = webdriver.Chrome()

# open Url
driver.get("https://www.amazon.co.uk/Palit-GamingPro-Graphics-DisplayPort-lighting/dp/B096KVBBHQ/ref=sr_1_5?crid=3A30EQU199NDN&keywords=3080+ti&qid=1658331824&sprefix=3080ti%2Caps%2C86&sr=8-5")
addToCart = driver.find_element("id", "add-to-cart-button")
time.sleep(1)
addToCart.click()
confirmClick = driver.find_element("xpath", "/html/body/div[5]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
time.sleep(0.5)
confirmClick.click()
