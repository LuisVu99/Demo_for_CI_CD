from pages.locators.login import LoginLocator
def test_verify_dashboard_page(login_page):
    assert login_page.is_dashboard_visible(), "Cannot login successfully"
