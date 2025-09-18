import allure


def test_incorrect_login_and_password(login_page):
    with allure.step("Открыть страницу логина"):
        login_page.open_page()

    with allure.step("Ввести неверные логин и пароль"):
        login_page.fill_login_form("123@123.com", "123123")

    with allure.step("Проверить сообщение об ошибке"):
        try:
            login_page.check_error_text("Authentication failed.")
        except AssertionError:
            # Делаем скриншот и прикладываем в отчёт
            screenshot = login_page.page.screenshot()
            allure.attach(
                screenshot,
                name="Ошибка авторизации",
                attachment_type=allure.attachment_type.PNG,
            )
            raise
