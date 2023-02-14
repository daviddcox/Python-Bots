import pyautogui as pt
import pydirectinput as pd
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = autoMineThread()
        self.autoMineButton = QPushButton('Start Mining', self)
        self.titles = []
        self.title = 'Minecraft Assist'
        self.left = 500
        self.top = 500
        self.width = 600
        self.height = 400
        self.initUI()
        self.layout = QVBoxLayout()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a button in the window
        self.autoMineButton.resize(150, 40)
        self.autoMineButton.move(100, 100)

        # connect button to function on_click
        self.autoMineButton.clicked.connect(self.auto_mine)
        self.show()

    @pyqtSlot()
    def auto_mine(self):
        self.worker.start()


def move(direction, dur):
    pd.keyDown(direction)
    time.sleep(dur)
    pd.keyUp(direction)



class autoMineThread(QThread):
    def run(self):
        time.sleep(1)
        pd.press('esc')
        pd.keyDown('shift')
        pd.mouseDown()
        while True:
            if pt.locateOnScreen('C:/Users/allen/Pictures/light0.jpg', confidence=.8) is None:
                pd.keyUp('shift')
                pd.mouseUp()
                move('s', 2)
                break
            else:
                move("w", .5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
