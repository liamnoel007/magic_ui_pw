from pages.base_page import BasePage
from pages.locators import login_locators as loc
from playwright.sync_api import expect


class Authentication(BasePage):

    page_url = "?controller=authentication&back=my-account"

    def fill_login_form(self, login, password):

        email_field = self.page.locator(loc.email_field_loc)
        password_field = self.page.locator(loc.password_field_loc)
        button = self.page.locator(loc.button_loc)

        email_field.fill(login)
        password_field.fill(password)
        button.click()

    def check_error_text(self, text):
        error = self.page.locator(f"//li[text()='{text}']")
        expect(error).to_contain_text(text)
