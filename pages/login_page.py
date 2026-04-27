from pages.base_page import BasePage
from pages.locators.login import LoginLocator

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_login(self):
        self.click(LoginLocator.LOGIN_NAV)

    def login(self, email: str, password: str,verify_login: str):
        self.fill(LoginLocator.LOGIN_EMAIL, email)
        self.fill(LoginLocator.LOGIN_PASS, password)
        self.click(LoginLocator.LOGIN_BUTTON)
        self.assert_text_contain(LoginLocator.VERIFY_LOGIN, verify_login)

    def signup(self, username: str, email: str, account_information: str, password: str, day: str,
               month: str, year: str, address_information: str, first_name: str, last_name: str, company: str, 
               address_1: str, address_2: str, country: str, state: str, city: str, zipcode: str, phone: str, verify_created: str, verify_login: str):
        #1. Click on forgot password
        self.fill(LoginLocator.SIGNUP_NAME, username)
        self.fill(LoginLocator.SIGNUP_EMAIL, email)
        self.click(LoginLocator.SIGNUP_BUTTON)
        self.assert_text_contain(LoginLocator.ACCOUNT_INFORMATION, account_information)
        self.click(LoginLocator.TITLE)
        self.fill(LoginLocator.PASS, password)
        self.select_value_dropdown(LoginLocator.DAY, day)
        self.select_value_dropdown(LoginLocator.MONTH, month)
        self.select_value_dropdown(LoginLocator.YEAR, year)
        self.click(LoginLocator.ENABLE_SIGNUP)
        self.click(LoginLocator.ENABLE_RECEIVE)
        self.assert_text_contain(LoginLocator.ADDRESS_INFORMATION, address_information)
        self.fill(LoginLocator.FIRST_NAME, first_name)
        self.fill(LoginLocator.LAST_NAME, last_name)
        self.fill(LoginLocator.COMPANY, company)
        self.fill(LoginLocator.ADDRESS, address_1)
        self.fill(LoginLocator.ADDRESS2, address_2)
        self.select_value_dropdown(LoginLocator.COUNTRY, country)
        self.fill(LoginLocator.STATE, state)
        self.fill(LoginLocator.CITY, city)
        self.fill(LoginLocator.ZIP, zipcode)
        self.fill(LoginLocator.PHONE, phone)
        self.click(LoginLocator.CREATE_BUTTON)
        self.assert_text_contain(LoginLocator.VERIFY_CREATED, verify_created)
        self.click(LoginLocator.CONTINUE_BUTTON)
        self.assert_text_contain(LoginLocator.VERIFY_LOGIN, verify_login)
        
    def logout(self, login_page: str):
        self.click(LoginLocator.LOGOUT)
        self.assert_have_text(LoginLocator.VERIFY_LOGIN_PAGE, login_page)

    def login_with_invalid_credential(self, email: str, password: str, expected_result:str):
        self.fill(LoginLocator.LOGIN_EMAIL, email)
        self.fill(LoginLocator.LOGIN_PASS, password)
        self.click(LoginLocator.LOGIN_BUTTON)
        self.assert_have_text(LoginLocator.INCORRECT_CREDENTIAL, expected_result)

    def delete_account(self, verify_deleted:str):
        self.click(LoginLocator.DELETE_ACCOUNT)
        self.assert_text_contain(LoginLocator.VERIFY_CREATED, verify_deleted)
        self.click(LoginLocator.CONTINUE_BUTTON)

    def signup_duplicated_email(self, username: str, email: str, duplicated_email: str):
        self.fill(LoginLocator.SIGNUP_NAME, username)
        self.fill(LoginLocator.SIGNUP_EMAIL, email)
        self.click(LoginLocator.SIGNUP_BUTTON)
        self.assert_have_text(LoginLocator.SIGNUP_DUPLICATED_EMAIL, duplicated_email)