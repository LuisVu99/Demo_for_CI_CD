from pages.login_page import LoginPage
from helpers.test_data import TestData

def test_signup(page):
    login_page = LoginPage(page)

    #1.Prepare Data
    username = TestData.random_user_name()
    email = TestData.random_email()
    account_information = "Enter Account Information"
    password = TestData.random_password()
    day = "10"
    month = "5"
    year = "1990"
    address_information = "Address Information"
    first_name = TestData.random_first_name()
    last_name= TestData.random_last_name()
    company = TestData.random_company()
    address_1 = TestData.randon_address()
    address_2 = TestData.randon_address()
    country = "United States"
    state = "California"
    city = "Los Angeles"
    zipcode = "90001"
    phone = TestData.randon_phone()
    verify_created = "Account Created!"
    verify_login = f"Logged in as {username}"
    #2. Navigate to Login/Signup
    login_page.navigate_to_login()    
    #3. Signup with valid information
    login_page.signup(username, email, account_information, password, day, month, year, address_information,
                      first_name, last_name, company, address_1, address_2, country, state, city,
                      zipcode, phone, verify_created, verify_login)