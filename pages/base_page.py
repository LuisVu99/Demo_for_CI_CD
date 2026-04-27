from playwright.sync_api import Page, expect
import time
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from config import ConfigUrl, BrowserConfig, Paths, ENVIRONMENTS

class BasePage:
    def __init__(self, page : Page):
        self.page = page
    
    def navigate(self, url : str):
        self.page.goto(url)
        
    def click(self, locator: str, force: bool = False):
        try:
            element = self.page.locator(locator)
            element.click(timeout=BrowserConfig.DEFAULT_TIMEOUT, force=force)
            print(f"Click successfully {locator}")
        except PlaywrightTimeoutError:
            raise Exception(f"Timeout: Cannot click {locator} within {BrowserConfig.DEFAULT_TIMEOUT} ms")
        except Exception as e:
            raise Exception(f"Failed to click {locator}: {e}")

    def fill(self, locator: str, text: str, force: bool = False):
        try:
            element = self.page.locator(locator)
            element.fill(text, timeout=BrowserConfig.DEFAULT_TIMEOUT, force = force)
            print(f"Fill successfully {locator} with text '{text}'")
        except PlaywrightTimeoutError:
            raise Exception(f"Timeout: Cannot fill {locator} within {BrowserConfig.DEFAULT_TIMEOUT} ms")
        except Exception as e:
            raise Exception(f"Failed to fill {locator}: {e}")

    def is_visible(self, locator: str) -> bool:
        visible = self.page.is_visible(locator)
        print(f"Element '{locator}' visible: {visible}")
        return visible
    
    def db_click(self, locator: str, force: bool = False):
            element = self.page.locator(locator)
            element.dblclick(timeout=BrowserConfig.DEFAULT_TIMEOUT, force=force)
    
    def wait_thread_sleep(self, seconds: float):
        time.sleep(seconds)

    def wait_for_load_page (self):
        self.page.wait_for_load_state("networkidle", timeout=BrowserConfig.DEFAULT_TIMEOUT)

    def wait_for_element_visible(self, locator: str):
        self.page.wait_for_selector(locator, state="visible", timeout=BrowserConfig.DEFAULT_TIMEOUT)

    def keyboard (self, key : str):
        self.page.keyboard.press(key)

    def assert_have_text(self, locator: str, exptected_text: str):
        element = self.page.locator(locator)
        try:
            expect(element).to_have_text(exptected_text, timeout=BrowserConfig.DEFAULT_TIMEOUT)
            print(f"Assert Passed: {locator} has text '{exptected_text}'")
        except AssertionError:
            print(f"Assert Failed: {locator} does not have text '{exptected_text}'")
            raise

    def assert_text_contain(self, locator: str, expected_substring: str):
        element = self.page.locator(locator)
        try:
            expect(element).to_contain_text(expected_substring, timeout=BrowserConfig.DEFAULT_TIMEOUT)
            print(f"Assert Passed: {locator} contains text '{expected_substring}'")
        except AssertionError:
            print(f"Assert Failed: {locator} does not contains text '{expected_substring}'")
            raise

    def assert_attribute(self, locator: str, name: str, expected_value: str, message = ""):
        self.wait_for_element_visible(locator)
        actual_value = self.page.locator(locator).get_attribute(name)
        assert actual_value == expected_value, (message or f"Value mismatch. Expected: '{expected_value}', but got: '{actual_value}")

    def assert_visible(self, locator: str):
        element = self.page.locator(locator)
        try:
            expect(element).to_be_visible(timeout=BrowserConfig.DEFAULT_TIMEOUT)
        except AssertionError:
            raise AssertionError(f"Element {locator} is not visible within {BrowserConfig.DEFAULT_TIMEOUT} ms")

    def assert_is_selected(self, locator: str):
        element = self.page.locator(locator)
        try:
            expect(element).to_be_checked(timeout=BrowserConfig.DEFAULT_TIMEOUT)
        except AssertionError:
            raise AssertionError(f"Element {locator} is not selected within {BrowserConfig.DEFAULT_TIMEOUT} ms")

    def upload_file(self, locator: str, file_path: str):
        self.page.set_input_files(locator, file_path)

    def select_value_dropdown(self, locator: str, value: str = None, label : str = None, index: int = None):
        self.wait_for_element_visible(locator)
        try:
            dropdown = self.page.locator(locator)
            if value:
                dropdown.select_option(value=value, timeout=BrowserConfig.DEFAULT_TIMEOUT)
                print(f"Selected by value: '{value}' in dropdown {locator}")
            elif label:
                dropdown.select_option(label = label, timeout=BrowserConfig.DEFAULT_TIMEOUT)
                print(f"Selected by label: '{label}' in dropdown {locator}")
            elif index:
                dropdown.select_option(index=index, timeout=BrowserConfig.DEFAULT_TIMEOUT)
                print(f"Selected by index: '{index}' in dropdown {locator}")
            else:
                raise ValueError("You must provide value, label, or index to select_option")
        except Exception:
            raise Exception(f"Cannot select value '{value}' in dropdown {locator}")
        #Use: self.select_value_dropdown("#country", value="VN")
            #self.select_value_dropdown("#country", label="Vietnam")
            #self.select_value_dropdown("#country", index=3)

    def handle_popup(self, action, accept=True, prompt_text=None, timeout=5000):
        """
        Xử lý popup khi thực hiện một action (click, v.v.).
        
        Args:
            page: đối tượng Page
            action: hàm hành động (vd: lambda: page.click("button"))
            accept: True = accept (OK), False = dismiss (Cancel)
            prompt_text: nếu popup là prompt thì nhập text
            timeout: thời gian chờ (ms)
        """
        dialog_message = None
        def dialog_handler(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message
            print(f"[Popup] Message: {dialog_message}")
            if prompt_text:
                dialog.accept(prompt_text=prompt_text)
            elif accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.on("dialog", dialog_handler)
        action()
        self.page.wait_for_timeout(timeout)
        return dialog_message

    def count_item_visible(self, locator: str):
        count = self.page.locator(locator).count()
        assert count >0, "No items found on the page"
        print(f"Found {count} items on the page")

    def verify_item_in_list(self, locator:str, keyword: str):
        results = self.page.locator(locator)
        count = results.count()
        assert count > 0, "No item found on the page"

        for i in range(count):
            item_text = results.nth(i).text_content().strip()
            print(f"Item {i+1}: {item_text}")
            assert keyword.lower() in item_text.lower(), f"Item '{item_text}'does not contain keyword '{keyword}'"

    def scroll_to_botton(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        print("Scrolled to bottom of the page")

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0,0)")
        print("Scrolled to top of the page")

    def delete_multiple_item(self, remove_button: str, item_attribute_name: str):
        while True:
            buttons = self.page.locator(remove_button)
            count = buttons.count()
            if count == 0:
                print("All items deleted successfully.")
                break

            btn = buttons.first
            product_id = btn.get_attribute(item_attribute_name)
            print(f"Deleting item with product_id={product_id}")
            btn.click()
            self.page.wait_for_timeout(1000)

    def download_and_verify(self, locator):
        with self.page.expect_download() as download_info:
            self.click(locator)
        download = download_info.value
        file_path = download.path()
        print("File downloaded at:", file_path)
        assert file_path is not None, "Download failed - no file path found"

    def verify_text_in_page_source(self, expected_text: str, wait_time: int = 5000):
        print(f"Waiting {wait_time}ms for page to render text...")
        self.page.wait_for_timeout(wait_time)
        page_source = self.page.content()

        if expected_text in page_source:
            print(f"✅ Success message found: '{expected_text}'")
        else:
            raise AssertionError(f"Could not find success message: '{expected_text}'")

    def drag_slider_with_keys(self, handle_locator: str, target_value: int, attribute_name: str = "aria-valuenow"):
        handle = self.page.locator(handle_locator)
        handle.click()

        # Lấy giá trị hiện tại từ attribute
        current_value = int(float(handle.get_attribute(attribute_name) or 0))

        # Nếu nhỏ hơn target → nhấn ArrowRight cho đến khi đạt target
        while current_value < target_value:
            handle.press("ArrowRight")
            current_value = int(float(handle.get_attribute(attribute_name) or 0))

        # Nếu lớn hơn target → nhấn ArrowLeft cho đến khi đạt target
        while current_value > target_value:
            handle.press("ArrowLeft")
            current_value = int(float(handle.get_attribute(attribute_name) or 0))

    def type_text(self, locator: str, text: str, delay: float = 0.1, clear: bool = True,):
        self.wait_for_element_visible(locator)
        element = self.page.locator(locator)
        element.click()
        if clear:
            element.fill("")
        for char in text:
            element.type(char, delay = delay)

    def hover_mouse_over(self, locator: str):
        self.wait_for_element_visible(locator)
        self.page.hover(locator)

    def fill_iframe(self, frame_locator: str, element_insider_iframe: str, text: str):
        self.wait_for_element_visible(frame_locator)
        frame = self.page.frame_locator(frame_locator)
        frame.locator(element_insider_iframe).fill(text)

    #Click sau 0,5s
    def click_after_duration(self, locator):
        self.page.locator(locator).wait_for(state="visible")
        self.page.wait_for_timeout(500)
        self.click(locator)

    def test_debug(self): 
        self.page.pause()

    def expect_url(self, url: str):
        expect(self.page).to_have_url(url)

    def expect_title(self, title: str):
        expect(self.page).to_have_title(title)



