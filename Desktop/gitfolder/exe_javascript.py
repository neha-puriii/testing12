from selenium import webdriver

from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

chromOptions= webdriver.ChromeOptions()
chromOptions.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromOptions)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.execute_script("window.scrollBy(0, 500)")
driver.get_screenshot_as_file("screen.png")
