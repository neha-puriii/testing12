from selenium import webdriver

from selenium.webdriver.chrome.service import service ,Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://paytm.com/")
print(driver.title)
driver.get("https://www.google.com/")
driver.back()
driver.refresh()
driver.forward()
driver.close()

