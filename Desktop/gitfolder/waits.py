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

#expexted_list = ['Cucumber - 1kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
#actualList = []
# implicit wait

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results: list[WebElement] = driver.find_elements(By.XPATH, "//div[@class='products']/div")
result: int = (len(results))
print(result)

assert result > 0

for result in results:
  #  actualList.append(result.find_element(By.XPATH, 'h4').text)
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()
time.sleep(5)
# explicit waits used for particular conditions where we have wait for maximum timemit is declare by creating class object webdriverwait(driver,10)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

# sum validation we convert str into int by follows these steps

prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalamt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalamt

# for validation
# driver.find_element(By.CSS_SELECTOR,".discountPerc").send_keys.('10%')
discAmt = float(driver.find_element(By.CSS_SELECTOR, '.discountAmt').text)

assert discAmt < totalamt
