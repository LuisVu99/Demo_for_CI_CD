from pages.login_page import LoginPage
from config import Credentials

def test_forgot_password(page):
    login_page = LoginPage(page)

    #1.Prepare Data
    username = "Luisvu"
    password = Credentials.ADMIN_EMAIL
    #2. Navigate to Login/Signup
    login_page.navigate_to_login()
    #3. Signup with duplicated email
    login_page.signup_duplicated_email(username, password, "Email Address already exist!")