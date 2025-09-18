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


import pytest
import allure


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        page_obj = None
        for arg in item.funcargs.values():

            if hasattr(arg, "page"):
                page_obj = arg
                break

        if page_obj:
            screenshot = page_obj.page.screenshot()
            allure.attach(
                screenshot,
                name=f"Скриншот-{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )
