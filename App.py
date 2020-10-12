import os
import tkinter

import feedparser
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic.properties import QtCore
from array import *

import designe  # Это наш конвертированный файл дизайна





class ExampleApp(QtWidgets.QMainWindow, designe.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.myFunction)
        self.urltext.setPlaceholderText("Введите url-rss адрес...")

        # Пока пустая функция которая выполняется
        # при нажатии на кнопку
    def myFunction(self):
        def parseRSS(rss_url):
            return feedparser.parse(rss_url)

        def getHeadlines(rss_url):
            headlines = []

            feed = parseRSS(rss_url)
            for newsitem in feed['items']:
                if self.checkBox_2.isChecked():
                    headlines.append(newsitem['title'])
                if self.checkBox_3.isChecked():
                    headlines.append(newsitem['link'])
                if self.checkBox_4.isChecked():
                    headlines.append(newsitem['id'])
                if self.checkBox_5.isChecked():
                    headlines.append(newsitem['summary'])
                if self.checkBox_6.isChecked():
                    headlines.append(newsitem['published'])

            return headlines

        allheadlines = []

        newsurls = {

            'googlenews': 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru',

        }

        for key, url in newsurls.items():
            allheadlines.extend(getHeadlines(url))
        if self.urltext.toPlainText() == 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru':
            for hl in allheadlines:
                lol = [hl]
                lol2 = ([hl])
                print(lol)
                print(lol2)
                self.outinfo.setPlainText(str(lol2))
                #print("-", hl)
                # dannie = self.urltext.toPlainText()
                # self.outinfo.setPlainText(hl)
                #while True:
                    #print("-", hl)
                    #self.outinfo.setText(hl)
                    #break
        else:
            from tkinter import messagebox
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Ошибка", "Неправильный url-rss адрес")
            print("lol")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
