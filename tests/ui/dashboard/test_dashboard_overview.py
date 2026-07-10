import allure
@allure.title("Luis test title")
def test_verify_dashboard_overview(dashboard_page):
    with allure.step("Step1")
    assert dashboard_page.is_menu_visible(), "Left menu is not displayed"
    with allure.step("Step2")
    assert dashboard_page.is_widget_visible(), "Widget Dashboard is not displayed"
    with allure.step("Step3")
    dashboard_page.search_name("Anh Tester")
