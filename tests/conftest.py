import pytest
import time
import json
import os
from playwright.sync_api import sync_playwright
from helpers.allure_helper import AllureHelper
from helpers.auth import AuthHelper, STORAGE_FILE
from tests.api.helpers.api_user import api_create_user, api_delete_user
from tests.api.helpers.api_template import api_create_template, api_delete_template
from tests.api.helpers.api_project import api_create_project
from tests.api.helpers.api_client import api_create_client, api_delete_client
from tests.api.helpers.api_task import api_create_task, api_delete_task
from config import ConfigUrl, BrowserConfig, Paths, ENVIRONMENTS, Credentials
from pages.login_page import LoginPage

#Browser list
BROWSER = ["chromium", "firefox", "webkit"]

STORAGE_FILE = Paths.STORAGE_FILE

def pytest_addoption(parser):
    """Thêm CLI option: chọn env, browser"""
    parser.addoption("--env", action="store", default="dev", help="dev/staging/prod")
    parser.addoption("--browser-name", action="store", default="chromium", help="chromium/firefox/webkit")
    parser.addoption("--record-video", action="store_true", help="Bật quay video khi chạy local")

@pytest.fixture
def env_config(request):
    env_name = request.config.getoption("--env")
    return ENVIRONMENTS[env_name]

@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser-name")

# --- Hook bắt lỗi để attach Allure ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def page_with_video(context, request):
    page = context.new_page(record_video_dir = "videos/")
    page.goto(ConfigUrl.base_url())
    yield page
    if hasattr(page, "video") and page.video:
        video_path = page.video.path()
    page.close()
    #attach video to allure
    if video_path:
        AllureHelper.attach_video(video_path, name=f"{request.node.name}_video")

@pytest.fixture(scope="session")
def browser(pytestconfig):
    """Khởi tạo Browser 1 lần cho cả session."""
    browser_name = pytestconfig.getoption("--browser-name")
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=BrowserConfig.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    """Mỗi test có 1 context riêng để isolation."""
    record_dir = os.path.join(os.getcwd(), "videos")
    os.makedirs(record_dir, exist_ok=True)

    context = browser.new_context(record_video_dir=record_dir)
    context.set_default_timeout(BrowserConfig.DEFAULT_TIMEOUT)
    context.set_default_navigation_timeout(BrowserConfig.DEFAULT_TIMEOUT)

    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    """Khởi tạo Page, luôn chụp screenshot, attach video khi fail."""
    page = context.new_page()
    page.goto(ConfigUrl.base_url())
    yield page

    # Always capture screenshot
    AllureHelper.attach_screenshot(page, f"{request.node.name}_screenshot")
    AllureHelper.attach_text("Final URL", page.url)

    # Only attach video if failed
    try:
        if request.node.rep_call.failed and page.video:
            video_path = page.video.path()
            AllureHelper.attach_video(video_path, name=f"{request.node.name}_video")
    except Exception:
        pass

    page.close()

@pytest.fixture(scope="function")
def login(page):
    """Login fixture - use this to automatically login before test.
    
    Usage in your test:
        def test_something(login):
            login.goto("some-url")
            ...
    """
    login_page = LoginPage(page)
    # Perform login with admin credentials
    login_page.navigate_to_login()
    login_page.login(Credentials.ADMIN_EMAIL, Credentials.ADMIN_PASSWORD, Credentials.ADMIN_USERNAME)
    # Return the logged-in page
    return page

@pytest.fixture(scope="function")
def login_page_instance(page):
    """LoginPage instance fixture - use this if you need to call LoginPage methods.
    
    Usage in your test:
        def test_something(login_page_instance):
            login_page_instance.login(email, password, verify_text)
            ...
    """
    return LoginPage(page)
    
def pytest_runtest_teardown(item, nextitem):
    time.sleep(2)

