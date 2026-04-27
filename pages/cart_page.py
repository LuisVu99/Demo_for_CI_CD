from pages.base_page import BasePage
from pages.locators.cart import CartLocator
from pages.locators.product import ProductLocator

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_cart(self):
        self.click(CartLocator.CARD_NAV)

    def add_item(self):
        self.click(CartLocator.ADD_FIRST_PRODUCT)
        self.click(CartLocator.CONTINUE_SHOPPING)
        self.click(CartLocator.ADD_SECOND_PRODUCT)
        self.click(CartLocator.VIEW_CART)

    def view_item(self, item_1_attribute_name: str, item_1_attribute_value: str, item_1_name: str,
                  item_1_price: str, item_1_quantity: str, item_1_total: str, item_2_attribute_name: str, 
                  item_2_attribute_value: str, item_2_name: str, item_2_price: str, item_2_quantity: str, item_2_total: str):
        #1. View product 1 in cart
        self.assert_attribute(CartLocator.ITEM_1_PICTURE, item_1_attribute_name, item_1_attribute_value)
        self.assert_have_text(CartLocator.ITEM_1_NAME, item_1_name)
        self.assert_have_text(CartLocator.ITEM_1_PRICE, item_1_price)
        self.assert_have_text(CartLocator.ITEM_1_QUANTITY, item_1_quantity)
        self.assert_have_text(CartLocator.ITEM_1_TOTAL, item_1_total)
        #1. View product 2 in cart
        self.assert_attribute(CartLocator.ITEM_2_PICTURE, item_2_attribute_name, item_2_attribute_value)
        self.assert_have_text(CartLocator.ITEM_2_NAME, item_2_name)
        self.assert_have_text(CartLocator.ITEM_2_PRICE, item_2_price)
        self.assert_have_text(CartLocator.ITEM_2_QUANTITY, item_2_quantity)
        self.assert_have_text(CartLocator.ITEM_2_TOTAL, item_2_total)

    def increase_item(self, quantity: str, item_total: str):
        self.click(ProductLocator.VIEW_PRODUCT_BUTTON)
        self.fill(CartLocator.QUANTITY_ITEM, quantity)
        self.click(CartLocator.ADD_TO_CART)
        self.click(CartLocator.VIEW_CART)
        self.assert_have_text(CartLocator.ITEM_1_QUANTITY, quantity)
        self.assert_have_text(CartLocator.ITEM_1_TOTAL, item_total)

    def delete_item(self, empty_card: str):
        self.wait_for_load_page()
        self.delete_multiple_item(CartLocator.DELETE_ITEM, "data-product-id")
        self.assert_text_contain(CartLocator.EMPTY_CARD, empty_card)

    def navigate_to_checkout(self):
        self.click(CartLocator.PROCEED_TO_CHECKOUT)
    
    def verify_address_detail(self, address_detail: str, deliver_address:str, delivery_company: str, delivery_name: str, delivery_address_1: str,
                               delivery_address_2: str, delivery_address_full: str, delivery_country: str, delivery_phone: str, billing_address: str,
                                billing_name: str, billing_company: str, billing_address_1: str, billing_address_2: str, billing_address_full: str,
                                 billing_country: str, billing_phone: str):
        self.assert_have_text(CartLocator.ADDRESS_DETAILS, address_detail)
        self.assert_have_text(CartLocator.DELIVERY_ADDRESS, deliver_address)
        self.assert_have_text(CartLocator.DELIVERY_COMPANY, delivery_company)
        self.assert_have_text(CartLocator.DELIVERY_NAME, delivery_name)
        self.assert_have_text(CartLocator.DELIVERY_COMPANY, delivery_company)
        self.assert_have_text(CartLocator.DELIVERY_ADDRESS_1, delivery_address_1)
        self.assert_have_text(CartLocator.DELIVERY_ADDRESS_2, delivery_address_2)
        self.assert_have_text(CartLocator.DELIVERY_ADDRESS_FULL, delivery_address_full)
        self.assert_have_text(CartLocator.DELIVERY_ADDRESS_COUNTRY, delivery_country)
        self.assert_have_text(CartLocator.DELIVERY_PHONE, delivery_phone)

        self.assert_have_text(CartLocator.BILLING_ADDRESS, billing_address)
        self.assert_have_text(CartLocator.BILLING_NAME, billing_name)
        self.assert_have_text(CartLocator.BILLING_COMPANY, billing_company)
        self.assert_have_text(CartLocator.BILLING_ADDRESS_1, billing_address_1)
        self.assert_have_text(CartLocator.BILLING_ADDRESS_2, billing_address_2)
        self.assert_have_text(CartLocator.BILLING_ADDRESS_FULL, billing_address_full)
        self.assert_have_text(CartLocator.BILLING_ADDRESS_COUNTRY, billing_country)
        self.assert_have_text(CartLocator.BILLING_PHONE, billing_phone)

    def review_order(self, item_1_attribute_name: str, item_1_attribute_value: str, item_1_name: str,
                  item_1_price: str, item_1_quantity: str, item_1_total: str, item_2_attribute_name: str, 
                  item_2_attribute_value: str, item_2_name: str, item_2_price: str, item_2_quantity: str, 
                  item_2_total: str, review_order: str, total_amount_text: str, total_price: str):
        self.assert_have_text(CartLocator.REVIEW_ORDER, review_order)
        self.view_item(item_1_attribute_name, item_1_attribute_value, item_1_name,
                  item_1_price, item_1_quantity, item_1_total, item_2_attribute_name, 
                  item_2_attribute_value, item_2_name, item_2_price, item_2_quantity, item_2_total)
        self.assert_have_text(CartLocator.TOTAL_AMOUNT_TEXT, total_amount_text)
        self.assert_have_text(CartLocator.TOTAL_PRICE, total_price)

    def add_comment(self, comment_description: str, comment_input: str):
        self.assert_have_text(CartLocator.COMMENT_DESCRIPTION, comment_description)
        self.fill(CartLocator.COMMENT_INPUT, comment_input)
        self.click(CartLocator.PLACE_ORDER)

    def add_recommended_item(self):
        self.scroll_to_botton()
        self.wait_for_element_visible(CartLocator.ADD_FIRST_RECOMMENDED_PRODUCT)
        self.click(CartLocator.ADD_FIRST_RECOMMENDED_PRODUCT)
        self.click(CartLocator.CONTINUE_SHOPPING)
        self.click(CartLocator.ADD_SECOND_RECOMMENDED_PRODUCT)
        self.click(CartLocator.VIEW_CART)

    def add_payment(self, payment_title: str, name_card: str, card_number: str, cvc: str
                    , expiration_month: str, expiration_year: str, successfully_order_payment: str):
        self.assert_have_text(CartLocator.PAYMENT_TITLE, payment_title)
        self.fill(CartLocator.NAME_CARD, name_card)
        self.fill(CartLocator.CARD_NUMBER, card_number)
        self.fill(CartLocator.CVC, cvc)
        self.fill(CartLocator.EXPIRATION_MONTH, expiration_month)
        self.fill(CartLocator.EXPIRATION_YEAR, expiration_year)
        self.click(CartLocator.CONFIRM_BUTTON)
        self.verify_text_in_page_source("Congratulations! Your order has been confirmed!")

    def verify_order_successfully(self, order_placed: str, successfully_order_message: str):
        self.assert_have_text(CartLocator.ORDER_PLACED, order_placed)
        self.assert_have_text(CartLocator.SUCCESSFULLY_ORDER_MESSAGE, successfully_order_message)
        self.download_and_verify(CartLocator.DOWNLOAD_INVOICE)
        self.click(CartLocator.CONTINUE_BUTTON)
            







