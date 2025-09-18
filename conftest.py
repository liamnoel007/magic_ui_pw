import pytest
from playwright.sync_api import Page
from pages.authentication import Authentication
from pages.t_shirts_page import TshirtsPage


@pytest.fixture()
def login_page(page):
    return Authentication(page)


@pytest.fixture()
def tshirt_page(page):
    return TshirtsPage(page)
