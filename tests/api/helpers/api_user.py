from playwright.sync_api import sync_playwright
import json
import os
import sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(ROOT_DIR)
from helpers.auth import STORAGE_FILE, AuthHelper
from config import ConfigUrl
from helpers.test_data import TestData

URL = ConfigUrl.USER_URL

def get_csrf_token(page):
    """Lấy CSRF token từ meta tag"""
    return page.eval_on_selector("meta[name='csrf-token']", "el => el.content")

def extract_user_id(response_body: str):
    """Lấy user_id từ response create user"""
    data = json.loads(response_body)
    html_value = data["dom_html"][0]["value"]
    return html_value.split('id="contacts_col_email_')[1].split('"')[0]

def api_create_user(page, first_name=None, last_name=None, email=None):
        first_name = first_name or TestData.random_first_name()
        last_name = last_name or TestData.random_last_name()
        email = email or TestData.random_email()

        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)
        
        post_data = (
            f"clientid=1&first_name={first_name}&last_name={last_name}"
            f"&email={email}&phone=0976765654&position=QA+Engineer"
            f"&timezone=Asia%2FHo_Chi_Minh&source="
        )

        response = page.request.post(
            URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Create user response:", response.status, response.headers)
        body = response.text()
        try:
            user_id = extract_user_id(body)
            print("Created user_id:", user_id)
        except Exception as e:
            print("Không lấy được user_id:", e)
            user_id = None

        data = {"first": first_name, "last": last_name, "email": email}
        return user_id, response, data

def api_delete_user(page, user_id: str):
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)
        post_data = "_method=DELETE"
        DELETE_USER_URL = f"{URL}/{user_id}"
        response = page.context.request.post(
            DELETE_USER_URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Response status:", response.status)
        return response
