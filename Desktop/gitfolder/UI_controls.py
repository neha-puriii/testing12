
from selenium import webdriver

from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break



radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

#Element displayed_

assert driver.find_element(By.ID,"show-textbox").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()




