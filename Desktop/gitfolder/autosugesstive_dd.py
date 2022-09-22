import time

from selenium import webdriver

from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys('ind')
time.sleep(1)
#for list

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))


for country in countries:
    if country.text == 'India' :
        country.click()
#to check the webelement we user get attribute
print(driver.find_element(By.ID, "autosuggest").get_attribute("Value"))
assert(driver.find_element(By.ID, "autosuggest").get_attribute("Value"))
