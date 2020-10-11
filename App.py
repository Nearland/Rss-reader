import os
import feedparser
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic.properties import QtCore

import designe  # Это наш конвертированный файл дизайна





class ExampleApp(QtWidgets.QMainWindow, designe.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.myFunction)

        # Пока пустая функция которая выполняется
        # при нажатии на кнопку
    def myFunction(self):
        def parseRSS(rss_url):
            return feedparser.parse(rss_url)

        def getHeadlines(rss_url):
            headlines = []

            feed = parseRSS(rss_url)
            for newsitem in feed['items']:
                headlines.append(newsitem['title'])
                # headlines.append(newsitem['link'])
                # headlines.append(newsitem['id'])
                # headlines.append(newsitem['summary'])
                # headlines.append(newsitem['published'])

            return headlines

        allheadlines = []

        newsurls = {

            'googlenews': 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru',

        }

        for key, url in newsurls.items():
            allheadlines.extend(getHeadlines(url))
        if self.urltext.toPlainText() == 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru':
            for hl in allheadlines:
                self.outinfo.setPlainText(hl)
                #print("-", hl)
                # dannie = self.urltext.toPlainText()
                # self.outinfo.setPlainText(hl)
                    #while True:
                        #print("-", hl)
                        #self.outinfo.setPlainText(hl)
                        #break
        else:
            print("lol")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
