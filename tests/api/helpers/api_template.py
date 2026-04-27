from playwright.sync_api import sync_playwright
import json
import pytest
import os
import sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(ROOT_DIR)
from helpers.auth import STORAGE_FILE, AuthHelper
from config import ConfigUrl

URL = ConfigUrl.TEMPLATE_URL

def get_csrf_token(page):
    """Lấy CSRF token từ meta tag"""
    token = page.eval_on_selector("meta[name='csrf-token']", "el => el.content")
    return token

def extract_template_id(response_body: str):
    """Lấy template_id từ response create template"""
    data = json.loads(response_body)
    html_value = data["dom_html"][0]["value"]
    template_id = html_value.split('id="project_')[1].split('"')[0]
    return template_id

def api_create_template(page, project_title = "Luis template_create"):
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)

        post_data = (
            f"project_title={project_title}&project_categoryid=1&manager=&project_description="
            "&show_more_settings_projects=&assignedperm_tasks_collaborate=&show_more_settings_projects2="
        )

        response = page.request.post(
            URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Create template response:", response.status, response.headers)
        body = response.text()
        try:
            template_id = extract_template_id(body)
            print("Created template_id:", template_id)
        except Exception as e:
            print("Không lấy được template_id:", e)
            template_id = None

        # browser.close()
        return template_id, response

def api_delete_template(page,template_id: str):
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)
        post_data = "_method=DELETE"
        DELETE_TEMPLATE_URL = f"https://demo.growcrm.io/templates/projects/{template_id}"

        response = page.context.request.post(
            DELETE_TEMPLATE_URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Response status:", response.status)

        # browser.close()
        return response

def save_response_body(response, filename="response_body.html"):
    """Lấy full body từ response và lưu ra file"""
    body = response.text()

    # Lưu vào file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(body)

    print(f"Đã lưu body vào file: {os.path.abspath(filename)}")
    return filename
