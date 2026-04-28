from pages.cart_page import CartPage
from pages.login_page import LoginPage
from helpers.test_data import TestData
from config import Credentials

def test_verify_address(login):
    cart_page = CartPage(login)

    #1. Prepare data
    #Use admin account information
    verify_login = f"Logged in as {Credentials.ADMIN_USERNAME}"
    
    #Address details:
    delivery_phone = "123456789"
    delivery_country = "United States"
    delivery_address_full = "Los Angeles California 90001"
    delivery_address_2 = "Apt 2"
    delivery_address_1 = "123 Main St"
    delivery_name = f"Mr. Luis Vu"
    delivery_company = "Tech Corp"
    address_detail = "Address Details"
    delivery_address = "Your delivery address"
    billing_address = "Your billing address"

    #Review order
    item_1_quantity = "1"
    item_1_price = "Rs. 500"
    item_1_name = "Blue Top"
    item_1_picture_name = "src"
    item_1_picture_value = "get_product_picture/1"
    item_1_total = "Rs. 500"

    item_2_total = "Rs. 1000"
    item_2_quantity = "1"
    item_2_price = "Rs. 1000"
    item_2_name = "Sleeveless Dress"
    item_2_picture_name = "src"
    item_2_picture_value = "get_product_picture/3"
    empty_card = "Cart is empty! Click here to buy products."
    review_order = "Review Your Order"
    total_amount_text = "Total Amount"
    total_price = "Rs. 1500"

    #Comment
    comment_input = "This is a comment of Luis"
    comment_description = "If you would like to add a comment about your order, please write it in the field below."
    #2. Already logged in via login fixture
    #3. Add product to cart
    cart_page.add_item()
    #4. Navigate to checkout page
    cart_page.navigate_to_checkout()
    #5. Verify delivery and billing address
    # cart_page.verify_address_detail(address_detail, delivery_address, delivery_company, delivery_name,
    #                                 delivery_address_1,delivery_address_2, delivery_address_full, delivery_country,
    #                                 delivery_phone, billing_address, delivery_name, delivery_company,
    #                                 delivery_address_1,delivery_address_2, delivery_address_full, delivery_country,
    #                                 delivery_phone)
    # cart_page.review_order(item_1_picture_name, item_1_picture_value, item_1_name, item_1_price, item_1_quantity, item_1_total,
    #                     item_2_picture_name, item_2_picture_value, item_2_name, item_2_price, item_2_quantity, item_2_total, review_order,
    #                     total_amount_text, total_price)
    cart_page.add_comment(comment_description, comment_input)
    #6. Delete order
    cart_page.navigate_to_cart()
    # cart_page.delete_item(empty_card)