import sys
from Scraping import Google
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, 
QPushButton, QAction, QLineEdit, QLabel, QVBoxLayout, QStackedWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Card(QWidget):
    def __init__(self, data, parent=None):
        QWidget.__init__(self, parent=parent)
        self.title='Google - Web Scraper'
        self.left=1
        self.top=1
        self.width=40
        self.height=10
        self.data=data
        
        title = QLabel(self.data['title'], self)
        url = QLabel(self.data['link'], self)
        description = QLabel(self.data['description'], self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(url)
        layout.addWidget(description)
 
        self.setLayout(layout)        

class Results(QMainWindow):
    def __init__(self, query):
        super().__init__()
        self.title='Google - Web Scraper'
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.query=query
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.statusBar().showMessage("Query - " + self.query)
        self.setGeometry(self.left,self.top,self.width,self.height)
        google = Google.Google()
        self.__data = google.scrape(self.query)

        self.layout = QVBoxLayout(self)
        self.Stack = QStackedWidget()
        for i in self.__data['results']:
            self.Stack.addWidget(Card(i))

        self.layout.addWidget(self.Stack)
        self.setCentralWidget(self.Stack)
        self.show()

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title='Google - Web Scraper'
        self.left=10
        self.top=10
        self.width=320
        self.height=100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.textbox=QLineEdit(self)
        self.textbox.move(15,15)
        self.textbox.resize(280,30)
        self.button=QPushButton('Search',self)
        self.button.move(110,55)
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue=self.textbox.text()
        self.dialog = Results(textboxValue)
        self.dialog.show()
        self.textbox.setText(textboxValue)

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())