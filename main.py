from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
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
driver.maximize_window()

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
time.sleep(3)
print("switch to fb_window login")
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(3)
# print(driver.title)

# deny cookies on fb window
time.sleep(3)
print("deny cookies on fb window")
fb_cookies_buttons = driver.find_elements(By.CSS_SELECTOR, "._9xo5 button")
deny_cookies_button = fb_cookies_buttons[0]
deny_cookies_button.click()

# log_in to fb
# enter email - username
time.sleep(3)
print("looking for and fill out username input")
email_input = driver.find_element(By.ID, "email")
email_input.send_keys(FACEBOOK_USERNAME)
# enter password
time.sleep(3)
print("looking for and fill out the password input")
password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(FACEBOOK_PASSWORD)
# looking for and click on "seconnecter button"
print("looking for and click on 'se connecter' button")
button_sign_in = driver.find_element(By.NAME, "login")
button_sign_in.click()

# switch back to base_window
time.sleep(3)
print("switch back to base_window")
driver.switch_to.window(base_window)
time.sleep(3)
# print(driver.title)


# allow tinder to access my location
print("allow tinder to access my location")
time.sleep(3)
try:
    allow_location_button = driver.find_element(By.XPATH, "//*[@id='q1979629556']/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
except NoSuchElementException:
    print("tinder is not asking for my location")
else:
    allow_location_button.click()

# allow notifications
print("dismiss notifications")
time.sleep(3)
try:
    dismiss_notifications_button = driver.find_element(By.XPATH, "//*[@id='q1979629556']/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
except NoSuchElementException:
    print("tinder is not asking to allow notifications")
else:
    dismiss_notifications_button.click()


# give time to close the pop_up chrome notifications
time.sleep(10)
print(driver.title)
print("catch body")
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.ARROW_LEFT)

# dislike people
for n in range(10):
    time.sleep(5)
    print(f"{n} people")
    body.send_keys(Keys.ARROW_LEFT)

