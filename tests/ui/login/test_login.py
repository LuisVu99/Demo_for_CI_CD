from pages.locators.login import LoginLocator
def test_verify_dashboard_page(login_page):
    login_page.expect_dash_board_visible()
