from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import zipfile

# Download and extract chrome driver 
urllib.request.urlretrieve("https://chromedriver.storage.googleapis.com/2.25/chromedriver_win32.zip", "chromedriver_win32.zip")
file = zipfile.ZipFile("chromedriver_win32.zip")
file.extractall()

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
searchBar = driver.find_element_by_id("masthead-search-term")
searchBar.send_keys("cat video")
searchBar.send_keys(Keys.ENTER)
time.sleep(5)
catLink = driver.find_element_by_css_selector("a[href='/watch?v=tntOCGkgt98']")
catLink.click()

