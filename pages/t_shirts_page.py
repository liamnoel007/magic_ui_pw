from pages.base_page import BasePage
from pages.locators import tshirts_locators as loc
from playwright.sync_api import expect


class TshirtsPage(BasePage):

    page_url = "?id_category=5&controller=category"

    def check_header_title_is(self, text):
        header_title = self.page.locator(loc.header_title_loc)
        expect(header_title).to_have_text(text)
