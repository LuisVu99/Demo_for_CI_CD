import os
import time
from playwright.sync_api import Page

from config import ConfigUrl, Paths
from pages.login_page import LoginPage
from pages.locators.dashboard import DashboardLocator


class LoginManager:
    _cookies = {}
    _last_login_time = {}
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_key_context(self, username, env):
        return f"{username}_{env}"

    def get_storage_path(self, env: str):
        base_name, ext = os.path.splitext(Paths.STORAGE_FILE)
        return os.path.abspath(f"{base_name}_{env}{ext}")

    def ensure_login(self, page: Page, username: str, password: str, env: str):
        if self.is_logged_in(page):
            return True

        context_key = self.get_key_context(username, env)
        if context_key in self._cookies and self.is_session_valid(context_key):
            try:
                page.context.add_cookies(self._cookies[context_key])
                page.goto(ConfigUrl.BASE_URL)
                if self.is_logged_in(page):
                    return True
            except Exception:
                pass

        self.perform_login(page, username, password, env)
        return True

    def is_session_valid(self, context_key: str, max_session_time: int = 1800):
        if context_key not in self._last_login_time:
            return False
        return time.time() - self._last_login_time[context_key] < max_session_time

    def is_logged_in(self, page):
        try:
            if page.url and "/login" not in page.url:
                if page.locator(DashboardLocator.LEFT_NAV_MENU).is_visible(timeout=1000):
                    return True
                if page.locator(DashboardLocator.WIDGET_OVERVIEW).is_visible(timeout=1000):
                    return True
        except Exception:
            pass

        return False

    def perform_login(self, page: Page, username: str, password: str, env: str):
        LoginPage(page).login(username, password)
        assert self.is_logged_in(page), "Cannot loggin successfully"
        context_key = self.get_key_context(username, env)
        self._cookies[context_key] = page.context.cookies()
        self._last_login_time[context_key] = time.time()
        page.context.storage_state(path=self.get_storage_path(env))
    