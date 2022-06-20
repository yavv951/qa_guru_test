from src.pages.base_page import BasePage
from src.pages.google_first_page import GoogleFirstPage


class Application:
    def __init__(self, base_url):
        self.url = base_url
        self.google_first_page = GoogleFirstPage(self)

    @staticmethod
    def close():
        BasePage.close()
