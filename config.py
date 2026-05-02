import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment name (dev, staging, prod, Developer)
ENVIRONMENT = os.getenv("ENVIRONMENT", "Developer")

class ConfigUrl:

    @staticmethod
    def base_url():
        base_url = os.getenv("BASE_URL")
        if not base_url:
            raise ValueError("BASE_URL is missing!")
        return base_url

    @classmethod
    def login_url(cls):
        return cls.base_url() + "/login"

    @classmethod
    def project_url(cls):
        return cls.base_url() + "/projects"

    @classmethod
    def client_url(cls):
        return cls.base_url() + "/clients"

    @classmethod
    def user_url(cls):
        return cls.base_url() + "/contacts"

    @classmethod
    def template_url(cls):
        return cls.base_url() + "/templates/projects"

    @classmethod
    def task_url(cls):
        return cls.base_url() + "/tasks"

# 2. Credentials (account test cố định)
class Credentials:
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "{{ADMIN_EMAIL_PLACEHOLDER}}")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "{{ADMIN_PASSWORD_PLACEHOLDER}}")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "{{ADMIN_USERNAME_PLACEHOLDER}}")
    USER_FULL_NAME = os.getenv("USER_FULL_NAME", "{{USER_FULL_NAME_PLACEHOLDER}}")
    USER_PASSWORD = os.getenv("USER_PASSWORD", "{{USER_PASSWORD_PLACEHOLDER}}")
    USER_USERNAME = os.getenv("USER_USERNAME", "{{USER_USERNAME_PLACEHOLDER}}")

# 3. Browser Settings
class BrowserConfig:
    HEADLESS = True
    DEFAULT_TIMEOUT = 30000
    VIEWPORT = {"width": 1920, "height": 1080}

# 4. API Config (nếu có test API)
class APIConfig:
    API_BASE_URL = "https://demo.growcrm.io/api"
    DEFAULT_HEADERS = {
        "Content-Type": "application/json"
    }

# 5. Other Constants (timeout, path, report)
class Paths:
    DOWNLOAD_DIR = "downloads/"
    REPORT_DIR = "reports/"
    STORAGE_FILE = "auth.json"