from selenium import webdriver

link = "https://accounts.google.com"
driver = webdriver.Chrome(executable_path='C:/Users/allen/.wdm/drivers/chromedriver')
driver.get(link)