import pytest
from src.pages.application import Application
from src.pages.base_page import BasePage

@pytest.fixture
def app(request):
    base_url = request.config.getoption("--base-url")
    BasePage.open_page(base_url)
    app = Application(base_url)
    yield app
    app.close()

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://google.com",
        help="enter base_url"
    )
