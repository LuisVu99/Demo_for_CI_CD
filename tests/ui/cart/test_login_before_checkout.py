from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from config import Credentials
from helpers.test_data import TestData

def test_login_before_checkout(page):
    cart_page = CartPage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    #1. Prepare data
    #Signup information
    username = Credentials.ADMIN_USERNAME
    email = TestData.random_email()
    account_information = "Enter Account Information"
    password = TestData.random_password()
    day = "10"
    month = "5"
    year = "1990"
    address_information = "Address Information"
    first_name = "Luis"
    last_name= "Vu"
    company = "Luis_company"
    address_1 = "Hanoi"
    address_2 = "Danang"
    country = "India"
    state = "Hoan Kiem"
    city = "Hanoi"
    zipcode = "10000"
    phone = "0987876761"
    verify_created = "Account Created!"
    verify_login = f"Logged in as {username}"
    verify_deleted = "Account Deleted!"
    #View product detail
    all_product = "All Products"
    product_name = "Sleeves Top"
    searched_product = "Searched Products"
    item_1_quantity = "1"
    item_1_price = "Rs. 359"
    item_1_name = "Half Sleeves Top Schiffli Detailing - Pink"
    item_1_picture_name = "src"
    item_1_picture_value = "get_product_picture/12"
    item_1_total = "Rs. 359"
    item_2_total = "Rs. 478"
    item_2_quantity = "1"
    item_2_price = "Rs. 478"
    item_2_name = "Sleeves Top and Short - Blue & Pink"
    item_2_picture_name = "src"
    item_2_picture_value = "get_product_picture/16"
    empty_card = "Cart is empty! Click here to buy products."

    #Address details:
    delivery_phone = phone
    delivery_country = country
    delivery_address_full = f"{city} {state} {zipcode}"
    delivery_address_2 = address_2
    delivery_address_1 = address_1
    delivery_name = f"Mr. {first_name} {last_name}"
    delivery_company = company
    address_detail = "Address Details"
    delivery_address = "Your delivery address"
    billing_address = "Your billing address"

    #Review order
    review_order = "Review Your Order"
    total_amount_text = "Total Amount"
    total_price = "Rs. 837"

    #Comment
    comment_input = "This is a comment of Luis"
    comment_description = "If you would like to add a comment about your order, please write it in the field below."

    #Checkout - Payment
    payment_title = "Payment"
    name_card = TestData.random_user_name()
    card_number = "41111111111"
    cvc = "1234"
    expiration_month = "12"
    expiration_year = "2040"
    successfully_order_payment = "Your order has been placed successfully!"
    #Successfully order
    successfully_order_message = "Congratulations! Your order has been confirmed!"
    order_placed = "Order Placed!"
    #2. Navigate and Login
    login_page.navigate_to_login()
    #3. Signup with valid information
    login_page.login(Credentials.ADMIN_EMAIL, Credentials.ADMIN_PASSWORD, verify_login)
    #4. Navigate to product
    product_page.navigate_to_product()
    #5. Search product
    product_page.search_product(product_name, searched_product)
    #6. Add item to product
    cart_page.add_item()
    #7. Verify product in cart
    cart_page.view_item(item_1_picture_name, item_1_picture_value, item_1_name, item_1_price, item_1_quantity, item_1_total,
                        item_2_picture_name, item_2_picture_value, item_2_name, item_2_price, item_2_quantity, item_2_total)
    #8. Checkout - Verify delivery and billing address
    cart_page.navigate_to_checkout()
    cart_page.verify_address_detail(address_detail, delivery_address, delivery_company, delivery_name,
                                    delivery_address_1,delivery_address_2, delivery_address_full, delivery_country,
                                    delivery_phone, billing_address, delivery_name, delivery_company,
                                    delivery_address_1,delivery_address_2, delivery_address_full, delivery_country,
                                    delivery_phone)
    cart_page.review_order(item_1_picture_name, item_1_picture_value, item_1_name, item_1_price, item_1_quantity, item_1_total,
                        item_2_picture_name, item_2_picture_value, item_2_name, item_2_price, item_2_quantity, item_2_total, review_order,
                        total_amount_text, total_price)
    cart_page.add_comment(comment_description, comment_input)
    #9. Checkout - Payment
    cart_page.add_payment(payment_title, name_card, card_number, cvc, expiration_month,
                          expiration_year, successfully_order_payment)
    #10. Verify Payment
    cart_page.verify_order_successfully(order_placed, successfully_order_message)

