from pages.cart_page import CartPage
from pages.product_page import ProductPage

def test_verify_quatity_item(page):
    cart_page = CartPage(page)
    product_page = ProductPage(page)

    #1. Prepare data
    all_product_title = "All Products"
    quantity = "4"
    item_total = "Rs. 2000"
    empty_card = "Cart is empty! Click here to buy products."
    #2. Add product to cart
    product_page.navigate_to_product()
    #3. Increase and Verify product in cart
    cart_page.increase_item(quantity, item_total)
    #4. Delete product in cart
    cart_page.delete_item(empty_card)

