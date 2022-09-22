from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
window2 = driver.window_handles[1]
driver.switch_to.window(window2)#to switch to new window
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
#to switch back to parent window
driver.switch_to.window(window2)
driver.find_element(By.TAG_NAME,"h3").text

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

