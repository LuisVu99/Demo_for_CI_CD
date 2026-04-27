from pages.cart_page import CartPage
from pages.login_page import LoginPage
from helpers.test_data import TestData

def test_verify_address(page):
    cart_page = CartPage(page)
    login_page = LoginPage(page)

    #1. Prepare data
    #Signup information
    username = TestData.random_user_name()
    email = TestData.random_email()
    account_information = "Enter Account Information"
    password = TestData.random_password()
    day = "10"
    month = "5"
    year = "1990"
    address_information = "Address Information"
    first_name = TestData.random_first_name()
    last_name= TestData.random_last_name()
    company = TestData.random_company()
    address_1 = TestData.randon_address()
    address_2 = TestData.randon_address()
    country = "United States"
    state = "California"
    city = "Los Angeles"
    zipcode = "90001"
    phone = TestData.randon_phone()
    verify_created = "Account Created!"
    verify_login = f"Logged in as {username}"
    verify_deleted = "Account Deleted!"

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
    #2. Navigate to Login/Signup
    login_page.navigate_to_login()    
    #3. Signup with valid information
    login_page.signup(username, email, account_information, password, day, month, year, address_information,
                      first_name, last_name, company, address_1, address_2, country, state, city,
                      zipcode, phone, verify_created, verify_login)
    #4. Add product to cart
    cart_page.add_item()
    #5. Navigate to checkout page
    cart_page.navigate_to_checkout()
    #6. Verify delivery and billing address
    cart_page.verify_address_detail(address_detail, delivery_address, delivery_company, delivery_name,
                                    delivery_address_1,delivery_address_2, delivery_address_full, delivery_country,
                                    delivery_phone, billing_address, delivery_name, delivery_company,
                                    delivery_address_1,delivery_address_2, delivery_address_full, delivery_country,
                                    delivery_phone)
    cart_page.review_order(item_1_picture_name, item_1_picture_value, item_1_name, item_1_price, item_1_quantity, item_1_total,
                        item_2_picture_name, item_2_picture_value, item_2_name, item_2_price, item_2_quantity, item_2_total, review_order,
                        total_amount_text, total_price)
    cart_page.add_comment(comment_description, comment_input)
    #7. Delete order
    cart_page.navigate_to_cart()
    cart_page.delete_item(empty_card)
    #8. Delete account
    login_page.delete_account(verify_deleted)
