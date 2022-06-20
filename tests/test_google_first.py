from src.models.first_page_model import FirstPageModel


class TestFirstPage:
    """
    Тест сьют. Тестирование странцы Google
    """

    def test_have_text_on_page(self, app):
        """
        Тест кейс 1111
        1. открыть страницу https://google.com
        2. ввести текст "selene"
        3. проверить, что на странице имеется текст 'Selene - User-oriented Web UI browser tests in Python'
        """
        field = FirstPageModel.random()
        app.google_first_page.input_values(field)
        app.google_first_page.check_have_text()


    def test_have_not_text_on_page(self, app):
        """
        Тест кейс 1111
        1. открыть страницу https://google.com
        2. ввести текст "selene"
        3. проверить, что на странице нет текста 'java'
        """
        field = FirstPageModel.random()
        app.google_first_page.input_values(field)
        app.google_first_page.check_invalid_text()




