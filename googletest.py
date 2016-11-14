from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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