import tkinter

import feedparser
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from tkinter import messagebox
import designe  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, designe.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.myFunction)
        self.urltext.setPlaceholderText("Введите url-rss адрес...")
        self.setFixedSize(800, 600)
        self.outinfo.setOpenExternalLinks(True)
        self.outinfo.setOpenLinks(True)

        # Пока пустая функция которая выполняется
        # при нажатии на кнопку

    def myFunction(self):
        def parseRSS(rss_url):
            return feedparser.parse(rss_url)

        def getHeadlines(rss_url):
            headlines = []

            feed = parseRSS(rss_url)
            for newsitem in feed['items']:
                if self.checkBox_2.isChecked():             # проверка check боксов
                    headlines.append(newsitem['title'])     # на активные / неактивные
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
            g = ""
            s = ""
            if self.urltext.toPlainText() == 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru':
                for hl in allheadlines:
                    s += "-" + hl + "\n"
                    g += "<a href=\"" + hl + "\">" + hl + "</a>"
                if self.checkBox_3.isChecked():
                    self.outinfo.setText(g)
                    print("-", g)
                else:
                    self.outinfo.setPlainText(s + "\n")
                    print("-", g)
            else:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo("Ошибка", "Неправильный url-rss адрес")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
