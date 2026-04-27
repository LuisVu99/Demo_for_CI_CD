from pages.test_case_page import CasePage

def test_navigate_case(page):
    test_case_page = CasePage(page)
    page_title = "Test Cases"
    #1 Navigate to Test Case page and verify title.
    test_case_page.verify_test_case(page_title)