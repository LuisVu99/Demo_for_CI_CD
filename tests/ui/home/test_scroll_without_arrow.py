from pages.home_page import HomePage
from helpers.test_data import TestData

def test_scroll_without_arrow(page):
    home_page = HomePage(page)
    #1. Prepare Data
    subscription = "Subscription"
    email = TestData.random_email()
    verify_successfully_message = "You have been successfully subscribed!"
    web_text = "Full-Fledged practice website for Automation Engineers"
    #2. verify scroll with arrow
    home_page.verify_scroll_without_arrow(subscription, email, verify_successfully_message, web_text)