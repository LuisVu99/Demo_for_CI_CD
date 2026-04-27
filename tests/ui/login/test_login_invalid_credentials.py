from pages.login_page import LoginPage
from helpers.test_data import TestData

def test_login_wrong_pass(page):
    login_page = LoginPage(page)

    #1.Prepare Data
    incorrect_email = TestData.random_email()
    incorrect_password = TestData.random_password()
    #2. Navigate to Login
    login_page.navigate_to_login()
    #3. Login with invalid credentials
    login_page.login_with_invalid_credential(incorrect_email, incorrect_password, "Your email or password is incorrect!")