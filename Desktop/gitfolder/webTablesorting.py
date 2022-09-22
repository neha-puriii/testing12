from selenium import webdriver
browserSortedList=[]
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebelements = driver.find_elements(By.XPATH,"//tr/td[1]")
for elements in veggieWebelements:
      browserSortedList.append(elements.text)

originalSortedList = browserSortedList.copy()
browserSortedList.sort()

assert   browserSortedList == originalSortedList
