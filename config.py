import os
from dotenv import load_dotenv

# Load environment variables from .env file (local development only)
load_dotenv()

# ============================================================================
# 1. ENVIRONMENT SELECTION
# ============================================================================
ENVIRONMENT = os.getenv("ENVIRONMENT", "developer") or "developer"

# ============================================================================
# 2. ENVIRONMENT STRUCTURE (All URLs from variables - no hardcoding)
# ============================================================================
ENVIRONMENTS = {
    "dev": {
        "url": os.getenv("DEV_BASE_URL"),  # From .env or GitHub variable
    },
    "staging": {
        "url": os.getenv("STAGING_BASE_URL"),  # From .env or GitHub variable
    },
    "prod": {
        "url": os.getenv("PROD_BASE_URL"),  # From .env or GitHub variable
    },
    "developer": {
        "url": os.getenv("base_url"),  # From .env or GitHub variable
    }
}

# ============================================================================
# 3. URLs CONFIG (derived from ENVIRONMENT)
# ============================================================================
class ConfigUrl:
    BASE_URL = ENVIRONMENTS[ENVIRONMENT]["url"]
    LOGIN_URL = BASE_URL + "/login"
    PROJECT_URL = BASE_URL + "/projects"
    CLIENT_URL = BASE_URL + "/clients"
    USER_URL = BASE_URL + "/contacts"
    TEMPLATE_URL = BASE_URL + "/templates/projects"
    TASK_URL = BASE_URL + "/tasks"

# ============================================================================
# 4. CREDENTIALS (sensitive - loaded from environment variables only)
# ============================================================================
class Credentials:
    # Local: load từ .env | CI/CD: load từ GitHub secrets
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    USER_FULL_NAME = os.getenv("USER_FULL_NAME")
    USER_PASSWORD = os.getenv("USER_PASSWORD")
    USER_USERNAME = os.getenv("USER_USERNAME")

# ============================================================================
# 5. BROWSER SETTINGS (non-sensitive defaults)
# ============================================================================
class BrowserConfig:
    HEADLESS = True
    DEFAULT_TIMEOUT = 30000
    VIEWPORT = {"width": 1920, "height": 1080}

# ============================================================================
# 6. API CONFIG (non-sensitive)
# ============================================================================
class APIConfig:
    API_BASE_URL = "https://demo.growcrm.io/api"
    DEFAULT_HEADERS = {
        "Content-Type": "application/json"
    }

# ============================================================================
# 7. PATHS & CONSTANTS (non-sensitive)
# ============================================================================
class Paths:
    DOWNLOAD_DIR = "downloads/"
    REPORT_DIR = "reports/"
    STORAGE_FILE = "auth.json"