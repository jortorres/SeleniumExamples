

from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element(By.LINK_TEXT, 'Sign in')
signin_link.click()

try:

    username_box = browser.find_element(By.ID, 'login_field')
    username_box.send_keys('Ninja')
    password_box = browser.find_element(By.ID, 'password')
    password_box.send_keys('NinjaPassword')
    password_box.submit()

except selenium.common.exceptions.NoSuchElementException:
        print("Error: Password Wrong")

except selenium.common.exceptions.NoSuchElementException:
        print("Error: Element not found")
finally:
        browser.quit()  

