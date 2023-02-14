from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("C:/Users/allen/.wdm/drivers/chromedriver/win32/97.0.4692.71/chromedriver.exe")
driver.get('https://wizardofodds.com/play/blackjack-v2/')
time.sleep(1000)

