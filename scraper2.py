import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
import sys


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.titles = []
        self.title = 'YouTube Comment'
        self.left = 500
        self.top = 500
        self.width = 600
        self.height = 400
        self.initUI()
        self.data = []
        self.textboxValue = ''
        self.layout = QVBoxLayout()
        self.number_comments = 0

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(150, 300, 200, 25)

        # Create textbox
        self.label = QLabel('YouTube URL:', self)
        self.label.move(10, 50)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.resize(180, 40)
        self.label.setStyleSheet('font-size: 20px')
        self.textbox = QLineEdit(self)
        self.textbox.move(180, 50)
        self.textbox.resize(280, 40)

        self.label2 = QLabel('Number of\nComments:', self)
        self.label2.move(10, 100)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.resize(180, 80)
        self.label2.setStyleSheet('font-size: 20px')
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(180, 120)
        self.textbox2.resize(280, 40)

        self.label3 = QLabel(self)
        self.label3.setText('Number of Youtube\nvideos searched: {}'.format(len(self.titles)))
        self.label3.move(10, 150)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.resize(180, 180)
        self.label3.setStyleSheet('font-size: 20px')

        # Create a button in the window
        self.button = QPushButton('Submit', self)
        self.button.resize(150, 40)
        self.button.move(380, 180)

        self.button2 = QPushButton('Move data to csv', self)
        self.button2.resize(150, 40)
        self.button2.move(380, 240)

        # connect button to function on_click
        self.button.clicked.connect(self.submit)
        self.button2.clicked.connect(self.upload_data_to_comments)
        print('hey there')
        self.show()

    @pyqtSlot()
    def submit(self):
        self.textboxValue = self.textbox.text()
        self.textbox.setText("")
        print(len(self.titles))
        self.titles.append(self.textboxValue)
        self.label3.setText('Number of Youtube\nvideos searched: {}'.format(len(self.titles)))
        self.number_comments = int(self.textbox2.text())
        self.search_for_comments()
        print('finished!')

    def search_for_comments(self):
        self.worker = MainBackgroundThread(self.textboxValue, self.number_comments)
        self.worker.start()

    @pyqtSlot()
    def upload_data_to_comments(self):
        print(self.data)
        print(self.titles)
        dic = {'video': self.titles, 'comments': self.data}
        df = pd.DataFrame(dic)
        df.to_csv('comments')


class MainBackgroundThread(QThread):
    def __init__(self, textboxValue, number_comments):
        QThread.__init__(self)
        self.textboxValue = textboxValue
        self.number_comments = number_comments

    def run(self):
        self.x = 2
        self.WINDOW_SIZE = "1920,1080"
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=%s" % self.WINDOW_SIZE)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        self.driver.get(self.textboxValue)
        self.textboxValue = ''
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(1)
        temporary_data = []
        progress = 1/self.number_comments * 100

        for i in range(self.number_comments):
            print('working...')
            element = "(//div[contains(@class,'style-scope ytd-expander')])[{}]".format(self.x)
            button = self.driver.find_element_by_xpath(element)
            print('working2...')
            actions = ActionChains(self.driver)
            actions.move_to_element(button).perform()
            print('working4...')
            temporary_data.append(self.driver.find_element_by_xpath(element).text)
            print('working3...')
            self.x += 1
            ex.pbar.setValue((i+1) * progress)
        ex.data.append(temporary_data)
        self.driver.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
