from pages.base_page import BasePage
from pages.locators.home import HomeLocator

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def verify_scroll_with_arrow(self, subscription: str, email: str, verify_successfully_message: str, web_text: str):
        self.scroll_to_botton()
        self.assert_have_text(HomeLocator.SUBSCRIPTION, subscription)
        self.fill(HomeLocator.EMAIL, email)
        self.click(HomeLocator.FORWARD_BUTTON)
        self.assert_have_text(HomeLocator.VERIFY_SUCCESSFUL, verify_successfully_message)
        self.click(HomeLocator.ARROW_UP)
        self.verify_item_in_list(HomeLocator.WEB_TEXT, web_text)

    def verify_scroll_without_arrow(self, subscription: str, email: str, verify_successfully_message: str, web_text: str):
        self.click(HomeLocator.NAVIGATE_CART)
        self.scroll_to_botton()
        self.assert_have_text(HomeLocator.SUBSCRIPTION, subscription)
        self.fill(HomeLocator.EMAIL, email)
        self.click(HomeLocator.FORWARD_BUTTON)
        self.assert_have_text(HomeLocator.VERIFY_SUCCESSFUL, verify_successfully_message)
        self.scroll_to_top()