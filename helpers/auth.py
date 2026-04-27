import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from config import ConfigUrl, Credentials, BrowserConfig, Paths

STORAGE_FILE = Paths.STORAGE_FILE

class AuthHelper:
    @staticmethod
    def ensure_logged_in():
        if not os.path.exists(STORAGE_FILE):
            AuthHelper.login_and_save_state()

    @staticmethod
    def login_and_save_state():
        with sync_playwright() as p:
            #Open Browser and Login by UI
            browser = p.chromium.launch(headless = BrowserConfig.HEADLESS)
            context = browser.new_context()
            page = context.new_page()
            page.goto(ConfigUrl.BASE_URL) 
            page.fill("#email", Credentials.ADMIN_USER)
            page.fill("#password", Credentials.ADMIN_PASSWORD)
            page.click("#loginSubmitButton")
            page.wait_for_url(ConfigUrl.BASE_URL + "/home", timeout=BrowserConfig.DEFAULT_TIMEOUT)
            # Save storage state (cookies + localStorage + sessionStorage)
            context.storage_state(path=STORAGE_FILE)
            print(f"✅ Saved to {STORAGE_FILE}")
            browser.close()
