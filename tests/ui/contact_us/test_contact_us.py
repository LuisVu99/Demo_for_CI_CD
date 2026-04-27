from pages.login_page import LoginPage
from pages.contact_us_page import ContactUsPage
from config import Credentials
from helpers.test_data import TestData

def test_contact_us(page):
    contact_us_page = ContactUsPage(page)
    get_in_touch = "Get In Touch"
    name = TestData.random_user_name()
    email = TestData.random_email()
    subject = "This is a subject"
    message = "This is a message"
    upload_file = "resources/time_module.png"
    verify_successfully = "Success! Your details have been submitted successfully."

    contact_us_page.contact_us(get_in_touch, name, email, subject, message, upload_file, verify_successfully)

