from pages.base_page import BasePage
from pages.locators.test_case import TestCaseLocator

class CasePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def verify_test_case(self,page_title: str):
        self.assert_visible(TestCaseLocator.HOME_PAGE)
        self.click(TestCaseLocator.TEST_CASE_PAGE)
        self.assert_have_text(TestCaseLocator.PAGE_TITLE, page_title)