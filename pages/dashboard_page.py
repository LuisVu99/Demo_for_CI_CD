from pages.base_page import BasePage
from pages.locators.dashboard import DashboardLocator

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def is_menu_visible(self):
        return self.is_visible(DashboardLocator.LEFT_NAV_MENU)

    def is_widget_visible(self):
        return self.is_visible(DashboardLocator.WIDGET_OVERVIEW)

    def search_name(self, text : str):
        # self.click(DashboardLocator.SEARCH_BOX)
        self.fill(DashboardLocator.SEARCH_BOX, text)
        # self.wait_thread_sleep(3)
        self.click(DashboardLocator.SEARCH_BUTTON)
        return self.search_name
        

