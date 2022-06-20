import time

from src.locators.google_first_page_locators import GoogleFirstPageLocators
from src.models.constants import Constants
from src.models.first_page_model import FirstPageModel
from src.pages.base_page import BasePage


class GoogleFirstPage(BasePage):
    """
    Главная страница
    """

    def input_values(self, data: FirstPageModel):
        if data.blank_text is not None: self.fill_element(GoogleFirstPageLocators.BLANK, data.blank_text)

    def check_have_text(self):
        self.check_element_have_text(GoogleFirstPageLocators.TEXT_ON_PAGE, Constants.TEXT)

    def check_invalid_text(self):
        self.condition_is_not_text(GoogleFirstPageLocators.TEXT_ON_PAGE, "java")

