from pages.base_page import BasePage
from pages.locators.login import LoginLocator
import allure

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Navigate to login page")
    def navigate_to_login(self):
        self.click(LoginLocator.LOGIN_NAV)

    @allure.step("Enter username and password, then click login button")
    def login(self, email: str, password: str):
        self.fill(LoginLocator.EMAIL, email)
        self.fill(LoginLocator.PASSWORD, password)
        self.click(LoginLocator.LOGIN_BUTTON)
        # Wait for dashboard nav to appear after successful login
        self.wait_for_element_visible(LoginLocator.DASHBOARD_NAV)

    @allure.step("Verify dashboard visible")
    def is_dashboard_visible(self):
        return self.is_visible(LoginLocator.DASHBOARD_NAV)
