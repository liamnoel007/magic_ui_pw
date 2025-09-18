def test_incorrect_login_and_password(login_page):
    @allure.step("Открыть страницу логина")
    login_page.open_page()
    @allure.step("Ввод неверный логина и пароля")
    login_page.fill_login_form("123@123.com", "123123")
    @allure.step("Проверка сообщения об ошибке")
    login_page.check_error_text("Authentication failed.")
