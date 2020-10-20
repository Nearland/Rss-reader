import App
import unittest


def URL_check(strr):
    return str(strr)


class TestApp(unittest.TestCase):

    def test_open_window(self):  # проверка на открытие приложения
        App.main()

    def test_error_messagebox(self):
        App.messagebox

    def test_app(self):
        App.ExampleApp

    def test_url_address(self):
        url = "https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru"
        self.assertEqual(URL_check(url), "https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru")  # проверка на
                                                                                                # правильность url


if __name__ == "__main__":
    unittest.main()
