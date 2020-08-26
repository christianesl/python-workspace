from selenium import webdriver
import time

browser = webdriver.Chrome("driver/chromedriver.exe")

browser.get('https://python.org')
time.sleep(5)
browser.quit()