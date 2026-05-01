from pages.product_page import ProductPage
from helpers.test_data import TestData

def test_reject_leave(page):
    product_page = ProductPage(page)

    #1.Prepare Data
    all_product_title = "All Products"
    write_review = "Write Your Review"
    name = TestData.random_user_name()
    email = TestData.random_email()
    add_review = "This is a review by Luis Vu"
    verify_successful = "Thank you for your review."

    #2. Navigate to product
    product_page.navigate_to_product()
    #3. Verify all product
    product_page.verify_all_product(all_product_title)
    #4. Add review
    product_page.add_review(write_review, name, email, add_review, verify_successful)