

from selenium import webdriver

from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice")
name ="nehaa"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys('name')
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alerts = driver.switch_to.alert
alert = (alerts.text)
print(alert)
alerts.dismiss()
assert 'name' in alert

