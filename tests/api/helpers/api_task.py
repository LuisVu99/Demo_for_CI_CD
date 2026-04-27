from playwright.sync_api import sync_playwright
import json
import pytest
import re
import os
import sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(ROOT_DIR)
from helpers.auth import STORAGE_FILE, AuthHelper
from config import ConfigUrl
from helpers.test_data import TestData

URL = ConfigUrl.TASK_URL

def get_csrf_token(page):
    """Lấy CSRF token từ meta tag"""
    token = page.eval_on_selector("meta[name='csrf-token']", "el => el.content")
    return token

def extract_task_id(response_body: str):
    """Lấy task_id từ response create task"""
    data = json.loads(response_body)
    html_value = data["dom_html"][0]["value"]
    task_id = html_value.split('id="card_task_')[1].split('"')[0]
    return task_id

def api_create_task(page, task_title = None):
        task_title = task_title or TestData.random_title()
        page.goto(URL)
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)

        post_data = (
            f"task_projectid=56"
            f"&task_title={task_title}"
            f"&task_status=3&task_priority=2&assigned%5B%5D=43&assigned-client%5B%5D=47"
            f"&show_more_settings_tasks=&task_description=&add_client_option_other=on"
            f"&task_custom_field_41=Low+Resolution&task_custom_field_42=Desktop&task_custom_field_51=1999"
            f"&task_custom_field_53=100&task_custom_field_32=&task_custom_field_21=Luis+test"
            f"&show_more_settings_tasks2=on&task_date_due=2025-08-12&tags%5B%5D=graphic-design"
            f"&task_client_visibility=on&task_billable=on&source=&ref="
        )

        response = page.request.post(
            URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Create task response:", response.status, response.headers)
        body = response.text()
        try:
            task_id = extract_task_id(body)
            print("Created task_id:", task_id)
        except Exception as e:
            print("Không lấy được task_id:", e)
            task_id = None

        data = {"title": task_title }
        return task_id, response, data

def api_delete_task(page, task_id: str):
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)
        post_data = "_method=DELETE"
        DELETE_TASK_URL = f"{URL}/{task_id}"

        response = page.context.request.post(
            DELETE_TASK_URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )
        print("Response status:", response.status)

        # browser.close()
        return response
