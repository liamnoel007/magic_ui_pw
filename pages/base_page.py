from playwright.sync_api import Page


class BasePage:

    base_url = "http://www.automationpractice.pl/index.php"
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Wrong page link")
