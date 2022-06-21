import os
from selenium import webdriver

os.environ['PATH'] += r"C:\SeleniumDrivers"


driver = webdriver.Chrome("C:/SeleniumDrivers/chromedriver.exe")
driver.get("https://www.pdfdrive.com/the-gifts-of-imperfection-embrace-who-you-are-e60365102.html")
my_element = driver.find_element_by_id('download_button_link')
my_element.click()