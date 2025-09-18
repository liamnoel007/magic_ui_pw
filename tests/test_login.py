import allure


@allure.feature("Авторизаци")
@allure.story("Авторизации недействительные учетные данные")
@allure.title("Тест формы ввода. Логин и пароль неверные")
@allure.severity(allure.severity_level.CRITICAL)
def test_incorrect_login_and_password(login_page):
    with allure.step("Открыть страницу логина"):
        login_page.open_page()

    with allure.step("Ввести неверные логин и пароль"):
        login_page.fill_login_form("123@123.com", "123123")

    with allure.step("Проверить сообщение об ошибке"):
        login_page.check_error_text("Authentication failed.")
