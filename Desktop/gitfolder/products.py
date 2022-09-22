import time
from typing import List

from selenium import webdriver

from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
productList = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for products in productList:
    productName= products.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        products.find_element(By.XPATH,"//div[@class='card h-100']/div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys('Ind')
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = (driver.find_element(By.CSS_SELECTOR,".alert").text)
print(message)
assert "Success" in message




