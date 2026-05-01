import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment name (dev, staging, prod, Developer)
ENVIRONMENT = os.getenv("ENVIRONMENT", "Developer")

# Define environments dict
ENVIRONMENTS = {
    "dev": {
        "url": "https://demo.growcrm.io",
        "username": "admin@example.com",
        "password": "growcrm"
    },
    "staging": {
        "url": "https://demo.growcrm.io",
        "username": "admin@example.com",
        "password": "growcrm"
    },
    "prod": {
        "url": "https://demo.growcrm.io",
        "username": "admin@example.com",
        "password": "growcrm"
    },
    "Developer": {
        "url": os.getenv("BASE_URL", "{{BASE_URL_PLACEHOLDER}}"),
        "username": "admin@example.com",
        "password": "growcrm"
    }
}

# 1. Environment Config (môi trường chạy test)
class ConfigUrl:
    BASE_URL = ENVIRONMENTS[ENVIRONMENT]["url"]
    LOGIN_URL = BASE_URL + "/login"
    PROJECT_URL = BASE_URL + "/projects"
    CLIENT_URL = BASE_URL + "/clients"
    USER_URL = BASE_URL + "/contacts"
    TEMPLATE_URL = BASE_URL + "/templates/projects"
    TASK_URL = BASE_URL + "/tasks"

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