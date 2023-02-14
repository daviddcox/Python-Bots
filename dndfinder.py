import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def main():
    keyword = "squid"
    keyword_list = []
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.shapeways.com/designer/mz4250/creations?s=0#more-products")
    time.sleep(.5)
    page_number = 1
    while True:
        time.sleep(1)
        for i in range(48):
            i += 1
            try:
                text = driver.find_element(By.XPATH, '(//a[@class="product-url"])[{}]'.format(i * 2)).text
                text = text.lower()
                if text.__contains__(keyword):
                    print(driver.current_url)
            except:
                e = 0
        page_number += 1
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH,
                                                                           '//span[@class="icon-chevron-right '
                                                                           'sw-dms--text-light"]'))


if __name__ == '__main__':
    main()
