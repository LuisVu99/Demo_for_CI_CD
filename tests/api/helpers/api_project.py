from playwright.sync_api import sync_playwright
import json
import pytest
import os
import sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(ROOT_DIR)
from helpers.auth import STORAGE_FILE, AuthHelper
from config import ConfigUrl
from helpers.test_data import TestData

URL = ConfigUrl.PROJECT_URL

def get_csrf_token(page):
    """Lấy CSRF token từ meta tag"""
    token = page.eval_on_selector("meta[name='csrf-token']", "el => el.content")
    return token

def extract_project_id(response_body: str):
    """Lấy project_id từ response create project"""
    data = json.loads(response_body)
    html_value = data["dom_html"][0]["value"]
    project_id = html_value.split('id="project_')[1].split('"')[0]
    return project_id #client_id

def api_create_project(page, company = None, first_name = None, last_name = None, email = None, project_title = None):
        company = company or TestData.random_company()
        first_name = first_name or TestData.random_first_name()
        last_name = last_name or TestData.random_last_name()
        email = email or TestData.random_email()
        project_title = project_title or TestData.random_title()
        
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)

        post_data = (
             f"project_clientid=&client_company_name={company}&first_name={first_name}&last_name={last_name}"
             f"&email={email}&add_client_option_other=&client_custom_field_1=&client_custom_field_11="
             f"&client_custom_field_21=&client_custom_field_41=&client-selection-type=new"
             f"&project_template_selector=-1628714745&project_title={project_title}&project_date_start=2024-12-13"
             f"&project_date_due=2026-11-18"
             f"&project_description=%3Cp%3E%3Cspan+style%3D%22text-decoration%3A+underline%3B%22%3E%3Cstrong"
             f"%3EProject+Brief%3C%2Fstrong%3E%3C%2Fspan%3E%3C%2Fp%3E%0A%3Cp%3EWe+are+looking+for+a+fresh+new+look"
             f"+for+our+juice+bottle+packaging.+Our+website+is+%3Ca+href%3D%22http%3A%2F%2Fwww.juicecompanysg."
             f"io%22%3Ehttp%3A%2F%2Fwww.juicecompanysg.io%3C%2Fa%3E%3C%2Fp%3E%0A%3Cul%3E%0A%3Cli%3EMorden+looking+"
             f"designs+with+fresh+vibrant+colours%3C%2Fli%3E%0A%3Cli%3EEmphasise+the+organic+nature+of+the+"
             f"drinks%3C%2Fli%3E%0A%3Cli%3EMust+include+bright+yellows+and+reds%3C%2Fli%3E%0A%3Cli%3EProvide+"
             f"images+in+high+resolution+(3000px+minimum)%3C%2Fli%3E%0A%3C%2Ful%3E%0A%3Cbr+%2F%3E%3Cbr+"
             f"%2F%3E%3Cspan+style%3D%22text-decoration%3A+underline%3B%22%3E%3Cstrong%3ETarget+Audience%3C%2Fstrong%3E%3C%2Fspan%3E%3Cbr+%2F%3E%3Cbr+%2F%3EOur+products+are+mostly+targeted+at+young+adults%3Cbr+%2F%3E%3Cbr+%2F%3E%3Cbr+%2F%3E%3Cbr+%2F%3E%3Cspan+style%3D%22text-decoration%3A+underline%3B%22%3E%3Cstrong%3EKeywords%2FTheme%3C%2Fstrong%3E%3C%2Fspan%3E%3Cbr+%2F%3E%3Cbr+%2F%3EWe+would+like+to+communicate+the+following%3A%3Cbr+%2F%3E%0A%3Cul%3E%0A%3Cli%3EOrganic%3C%2Fli%3E%0A%3Cli%3E100%25+fruit%3C%2Fli%3E%0A%3Cli%3ENo+added+sugar%3C%2Fli%3E%0A%3Cli%3ENo+preservatives+or+artificial+colouring%3C%2Fli%3E%0A%3Cli%3EHealthy%3C%2Fli%3E%0A%3Cli%3EEnergy+booster%3C%2Fli%3E%0A%3C%2Ful%3E%0A%3Cbr+%2F%3E%0A%3Cp%3E%3Cspan+style%3D%22text-decoration%3A+underline%3B%22%3E%3Cstrong%3ETimeframes%3C%2Fstrong%3E%3C%2Fspan%3E%3C%2Fp%3E%0A%3Cp%3EWe+are+looking+to+launch+the+new+designs+in+3+months+time%3Cbr+%2F%3E%3Cbr+%2F%3E%3Cbr+%2F%3E%3C%2Fp%3E%0A%3Chr+%2F%3E%0A%3Cp%3E%3Cbr+%2F%3E%3Cspan+style%3D%22text-decoration%3A+underline%3B%22%3E%3Cstrong%3ESample+Designs%3Cbr+%2F%3E%3Cbr+%2F%3E%3C%2Fstrong%3E%3C%2Fspan%3EBelow+are+some+products+that+have+a+similar+design+to+what+we+are+looking+for.%3Cbr+%2F%3E%3Cbr+%2F%3E%3Cimg+src%3D%22storage%2Ffiles%2Fmx0dQrSK0Rtt2VJq06sVAs14nWq1JE3BYI4kmwal%2Fimg.jpg%22+alt%3D%22%22+width%3D%22809%22+height%3D%22472%22+%2F%3E%3Cbr+%2F%3E%3Cbr+%2F%3E%3C%2Fp%3E%0A%3Cp%3E%26nbsp%3B%3C%2Fp%3E&project_categoryid=1&manager=&project_progress_manually=on&project_progress=87.00&project_billing_rate=0.00&project_billing_type=hourly&project_billing_estimated_hours=0&project_billing_costs_estimate=0.00&show_more_settings_projects=&assignedperm_tasks_collaborate=on&show_more_settings_projects2=&clientperm_tasks_view=&clientperm_tasks_collaborate=on&clientperm_tasks_create=&clientperm_checklists=&clientperm_timesheets_view=&clientperm_expenses_view=&source=&project_custom_field_1=&project_custom_field_42=&project_custom_field_43=&project_custom_field_41=&project_custom_field_51=&project_custom_field_52=&project_custom_field_22=&show_after_adding=on"
        )

        response = page.request.post(
            URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Create project response:", response.status, response.headers)
        body = response.text()
        try:
            project_id = extract_project_id(body)
            print("Created project_id:", project_id)
            html_value = extract_project_id(body)
            print("===== DOM_HTML VALUE =====")
            print(html_value)
            # print("Created client_id:", client_id)
        except Exception as e:
            print("Không lấy được project_id:", e)
            project_id = None
        
        data = {"company": company, "first": first_name, "last": last_name, "email": email, "title": project_title}

        return project_id, response, data

def api_delete_project(page, project_id: str):
        csrf_token = get_csrf_token(page)
        print("CSRF token:", csrf_token)
        post_data = "_method=DELETE"
        DELETE_project_URL = f"{URL}/{project_id}"

        response = page.context.request.post(
            DELETE_project_URL,
            data=post_data,
            headers={
                "X-CSRF-TOKEN": csrf_token,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )

        print("Response status:", response.status)
        return response
