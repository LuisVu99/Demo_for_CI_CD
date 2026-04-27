from pages.base_page import BasePage
from pages.locators.contact_us import ContactUsLocator

class ContactUsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def contact_us(self, get_in_touch: str, name: str, email: str, subject: str, message: str,
                   upload_file:str, verify_successfully:str):
        # self.assert_visible(ContactUsLocator.HOME_PAGE)
        self.click(ContactUsLocator.CONTACTUS_PAGE)
        self.wait_thread_sleep(3)
        self.assert_have_text(ContactUsLocator.GET_IN_TOUCH, get_in_touch)
        self.fill(ContactUsLocator.NAME, name)
        self.fill(ContactUsLocator.EMAIL, email)
        self.fill(ContactUsLocator.SUBJECT, subject)
        self.fill(ContactUsLocator.YOUR_MESSAGE, message)
        self.upload_file(ContactUsLocator.UPLOAD_FILE, upload_file)
        self.handle_popup(
            lambda: self.click(ContactUsLocator.SUBMIT_BUTTON, force=True),
            accept=True
        )
        self.assert_have_text(ContactUsLocator.VERIFY_SUBMIT_SUCCESSFULLY, verify_successfully)
        self.click(ContactUsLocator.HOME_BUTTON)
        # self.assert_visible(ContactUsLocator.HOME_PAGE)

