from selenium import webdriver
from datetime import date
import time
from selenium.webdriver.common.action_chains import ActionChains


class Course:
    def __init__(self):
        self.driver_path = 'C:/Users/Allen/webdrivers/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.search_date = ""
        self.main_window = self.driver.current_window_handle

    def click(self, element):
        button = self.driver.find_element_by_xpath(element)
        button.click()

    def type(self, element, text):
        button = self.driver.find_element_by_xpath(element)
        button.send_keys(text)

    def quiz(self, url):
        today = date.today()
        month = today.strftime("%m")
        month = int(month)
        month = str(month)
        day = today.strftime("%d")
        day = int(day)
        day = str(day)
        year = today.strftime("%Y")
        self.search_date = "'" + month + "-" + day + "-" + year + "'"
        self.driver.get(url)
        time.sleep(3)
        button = self.driver.find_element_by_xpath("//a[contains(., " + self.search_date + ")]")
        actions = ActionChains(self.driver)
        actions.move_to_element(button).perform()
        button.click()
        time.sleep(2)

    def open_tab(self):
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)

    def google(self, url):
        self.driver.get(url)
        time.sleep(.2)

    def check_available(self, element):
        button = self.driver.find_element_by_xpath(element)
        actions = ActionChains(self.driver)
        actions.move_to_element(button).perform()
        text = self.driver.find_element_by_xpath(element).text
        return text
