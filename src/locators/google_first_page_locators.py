from selene.support import by
from selenium.webdriver.common.by import By


class GoogleFirstPageLocators:
    BLANK = by.css('[name="q"]')
    TEXT_ON_PAGE = by.css('[id="search"]')
