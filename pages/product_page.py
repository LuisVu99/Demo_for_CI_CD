from pages.base_page import BasePage
from pages.locators.product import ProductLocator

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_product(self):
        self.click(ProductLocator.PRODUCT_NAV)

    def verify_all_product(self, all_product_title: str):
        self.assert_have_text(ProductLocator.ALL_PRODUCT_TITLE, all_product_title)
        self.count_item_visible(ProductLocator.PRODUCT_LIST)

    def view_product_detail(self, attribute_picture: str, attribute_picture_value: str, attribute_new_label: str, attribute_new_label_value: str,
                            product_name:str, category:str, price:str, availability:str, condition:str, brand:str):
        self.click(ProductLocator.VIEW_PRODUCT_BUTTON)
        self.assert_attribute(ProductLocator.PRODUCT_PICTURE, attribute_picture, attribute_picture_value)
        self.assert_attribute(ProductLocator.NEW_LABEL, attribute_new_label, attribute_new_label_value)
        self.assert_have_text(ProductLocator.VIEW_PRODUCT_NAME, product_name)
        self.assert_have_text(ProductLocator.CATEGORY, category)
        self.assert_have_text(ProductLocator.PRICE, price)
        self.assert_have_text(ProductLocator.AVAILABILITY, availability)
        self.assert_have_text(ProductLocator.CONDITION, condition)
        self.assert_have_text(ProductLocator.BRAND, brand)

    def add_review(self, write_review: str, name: str, email: str, add_review:str, verify_successful:str):
        self.click(ProductLocator.VIEW_PRODUCT_BUTTON)
        self.assert_have_text(ProductLocator.WRITE_REVIEW, write_review)
        self.fill(ProductLocator.YOUR_NAME, name)
        self.fill(ProductLocator.EMAIL_ADDRESS, email)
        self.fill(ProductLocator.ADD_REVIEW, add_review)
        self.click(ProductLocator.SUBMIT_BUTTON)
        self.assert_have_text(ProductLocator.VERIFY_SUCCESSFUL, verify_successful)

    def search_product(self, product_name: str, searched_product:str):
        self.fill(ProductLocator.SEARCH_BOX, product_name)
        self.click(ProductLocator.SEARCH_BUTTON)
        self.assert_have_text(ProductLocator.SEARCHED_PRODUCT, searched_product)
        self.verify_item_in_list(ProductLocator.PRODUCT_NAME, product_name)

    def verify_product_category(self, verify_category_all: str, verify_women_category: str, verify_women_product:str,
                                verify_men_category: str, verify_men_product:str):
        #1. Verify women category
        self.assert_have_text(ProductLocator.VERIFY_CATEGORY, verify_category_all)
        self.click(ProductLocator.CLICK_WOMEN)
        self.click(ProductLocator.CLICK_DRESS)
        self.assert_have_text(ProductLocator.VERIFY_CATEGORY_TITLE, verify_women_category)
        self.assert_have_text(ProductLocator.VERIFY_PRODUCT_TITLE, verify_women_product)
        self.click(ProductLocator.VIEW_PRODUCT_BUTTON)
        self.assert_text_contain(ProductLocator.CATEGORY, verify_women_category)
        #2. Verify man category
        self.click(ProductLocator.CLICK_MEN)
        self.click(ProductLocator.CLICK_TSHIRTS)
        self.assert_have_text(ProductLocator.VERIFY_CATEGORY_TITLE, verify_men_category)
        self.assert_have_text(ProductLocator.VERIFY_PRODUCT_TITLE, verify_men_product)
        self.click(ProductLocator.VIEW_PRODUCT_BUTTON)
        self.assert_text_contain(ProductLocator.CATEGORY, verify_men_category)

    def verify_product_brand(self, verify_brand_all: str, verify_brand_title: str, verify_madame_product:str):
        self.assert_have_text(ProductLocator.VERIFY_BRANDS, verify_brand_all)
        self.click(ProductLocator.CLICK_MADAME)
        self.assert_have_text(ProductLocator.VERIFY_BRAND_TITLE, verify_brand_title)
        self.assert_have_text(ProductLocator.VERIFY_PRODUCT_TITLE, verify_madame_product)
        self.count_item_visible(ProductLocator.PRODUCT_LIST)
        self.click(ProductLocator.VIEW_PRODUCT_BUTTON)
        self.assert_text_contain(ProductLocator.BRAND, verify_brand_title)


