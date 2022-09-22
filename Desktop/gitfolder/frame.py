
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/iframe")
wait = WebDriverWait(driver,30)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"mce_0_ifr")))

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("myself neha")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)

