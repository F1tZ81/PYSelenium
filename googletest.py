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
driver.get("http://www.google.com")
assert "Google" in driver.title
searchBar = driver.find_element_by_name("q")
searchBar.send_keys("OST Grand Rapids")
searchBar.send_keys(Keys.ENTER)
time.sleep(5)
assert "an information technology leader" in driver.page_source
time.sleep(30)
driver.close()