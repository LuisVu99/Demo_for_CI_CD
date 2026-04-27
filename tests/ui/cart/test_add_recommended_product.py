from pages.cart_page import CartPage

def test_add_recommended_product(page):
    cart_page = CartPage(page)

    #1. Prepare data
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
    #2. Add product to cart
    cart_page.add_recommended_item()
    #3. Verify product in cart
    cart_page.view_item(item_1_picture_name, item_1_picture_value, item_1_name, item_1_price, item_1_quantity, item_1_total,
                        item_2_picture_name, item_2_picture_value, item_2_name, item_2_price, item_2_quantity, item_2_total)
    #4. Delete product in cart
    cart_page.delete_item(empty_card)