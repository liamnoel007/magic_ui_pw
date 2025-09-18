def test_incorrect_login_and_password(login_page):
    login_page.open_page()
    login_page.fill_login_form("123@123.com", "123123")
    login_page.check_error_text("Authentication failed.")
