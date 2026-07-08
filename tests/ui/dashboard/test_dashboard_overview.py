def test_verify_dashboard_overview(dashboard_page):
    assert dashboard_page.is_menu_visible(), "Left menu is not displayed"
    assert dashboard_page.is_widget_visible(), "Widget Dashboard is not displayed"
    dashboard_page.search_name("Anh Tester")
