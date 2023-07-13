import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure you have installed Chrome WebDriver and its path is set

# Open the yahoo website
driver.get("https://www.yahoo.com")
time.sleep(2)
# clcik mail button
mail = driver.find_element("xpath", "//a[text()='Sign in']")
time.sleep(5)
mail.click()

#Enter username
username = driver.find_element("id","login-username")
username.send_keys("Victor@yahoo.com")
time.sleep(2)

#Click Next Button
nextButton = driver.find_element("xpath", "//input[@name='signin']")
nextButton.click()
time.sleep(5)

#Close the browser
driver.quit()
