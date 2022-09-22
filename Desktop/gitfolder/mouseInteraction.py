
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
actions: ActionChains = ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH ,"//button[@id='mousehover']")).perform()
 #actions.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
