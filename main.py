from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

FACEBOOK_USERNAME = os.environ["FACEBOOK_USERNAME"]
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]
CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
# chrome_driver_path = r"C:\Users\Utilisateur1\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://tinder.com/fr")

# deny cookies with XPATH
time.sleep(5)
print("Select the deny cookies button")
deny_cookies_button = driver.find_element(By.XPATH, "//*[@id='q-586956664']/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]")
deny_cookies_button.click()

# click on connection button
time.sleep(3)
print("click on connection button")
connection_button = driver.find_element(By.XPATH, "//*[@id='q-586956664']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
connection_button.click()

# select facebook connection
time.sleep(3)
print("select facebook connection")
facebook_button = driver.find_element(By.XPATH, "//*[@id='q1979629556']/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]")
facebook_button.click()

# catch_up the fb window connection
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)



