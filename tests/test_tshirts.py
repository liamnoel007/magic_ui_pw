def test_header_title(tshirt_page):
    tshirt_page.open_page()
    tshirt_page.check_header_title_is("T-shirts")
