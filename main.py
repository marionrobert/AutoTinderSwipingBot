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