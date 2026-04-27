from playwright.sync_api import sync_playwright
import json
import os
import sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(ROOT_DIR)
from config import ConfigUrl
from helpers.test_data import TestData

URL = ConfigUrl.CLIENT_URL

def get_csrf_token(page):
    """Lấy CSRF token từ meta tag"""
    return page.eval_on_selector("meta[name='csrf-token']", "el => el.content")

def extract_client_id(response_body: str):
    """Lấy client_id từ response create client"""
    data = json.loads(response_body)
    html_value = data["dom_html"][0]["value"]
    return html_value.split('id="clients_col_id_')[1].split('"')[0]

def api_create_client(page, company_name = None, first_name = None , last_name = None, email = None):
        company_name = company_name or TestData.random_company()
        first_name = first_name or TestData.random_first_name()
        last_name = last_name or TestData.random_last_name()
        email = email or TestData.random_email()
        
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)
        post_data = (
            f"client_company_name={company_name}&first_name={first_name}&last_name={last_name}&email={email}"
            f"&client_categoryid=68&client_description=&add_client_option_bill_address="
            f"&client_billing_street=&client_billing_city=&client_billing_state=&client_billing_zip="
            f"&client_billing_country=&client_phone=&client_website=&client_vat=&add_client_option_shipping_address="
            f"&client_shipping_street=&client_shipping_city=&client_shipping_state=&client_shipping_zip=&client_shipping_country="
            f"&same_as_billing_address=&add_client_option_other=&client_app_modules=system&client_settings_modules_projects=on"
            f"&client_settings_modules_invoices=on&client_settings_modules_payments=on&client_settings_modules_knowledgebase=on"
            f"&client_settings_modules_estimates=on&client_settings_modules_subscriptions=on"
            f"&client_settings_modules_tickets=on&client_custom_field_1=&client_custom_field_11="
            f"&client_custom_field_21=&client_custom_field_41="
        )

        response = page.context.request.post(
            URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Create client response:", response.status, response.headers)
        body = response.text()
        try:
            client_id = extract_client_id(body)
            print("Created client_id:", client_id)
        except Exception as e:
            print("Không lấy được client_id:", e)
            client_id = None
        data = {"company": company_name, "first": first_name, "last": last_name, "email": email}
        return client_id, response, data

def api_delete_client(page, client_id: str):
        # page.goto(CLIENT_URL)
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)
        post_data = "_method=DELETE"
        DELETE_CLIENT_URL = f"{URL}/{client_id}"
        response = page.context.request.post(
            DELETE_CLIENT_URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )
        return response
