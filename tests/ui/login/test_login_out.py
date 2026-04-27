from pages.login_page import LoginPage
from config import Credentials

def test_login(page):
    login_page = LoginPage(page)

    #1. Navigate to Login
    login_page.navigate_to_login()
    #2. Login
    login_page.login(Credentials.ADMIN_EMAIL, Credentials.ADMIN_PASSWORD, "Logged in as Luis Vu")
    #3. Logout
    login_page.logout("Login to your account")