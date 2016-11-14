Small Example of Pyhton Selenium

# Install
## Windows
Install Python from [Windows Python Site](http://www.python.org/download)

## Selenium
In any command line type

    pip install selenium
    
Mkae sure you have [Chrome Browser](https://www.google.com/chrome/browser/desktop/) installed

# Example
Create a file called googletest.py place this example code in that file:

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

## Run
from the command line type

    python googletest.py

# More information
[Seleium Python Bindings](http://selenium-python.readthedocs.io/index.html)

[Seleium Site](http://www.seleniumhq.org/projects/webdriver/)

[VS Code](https://code.visualstudio.com/)

[Git](https://git-scm.com/)
