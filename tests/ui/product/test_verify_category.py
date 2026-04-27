from pages.product_page import ProductPage

def test_verify_category(page):
    product_page = ProductPage(page)

    #1.Prepare Data
    all_product_title = "All Products"
    verify_category_all = "Category"
    verify_women_category = "Women > Dress"
    verify_women_product = "Women - Dress Products"
    verify_men_category = "Men > Tshirts"
    verify_men_product = "Men - Tshirts Products"
    #2. Navigate to product
    product_page.navigate_to_product()
    #3. Verify all product
    product_page.verify_all_product(all_product_title)
    #4. View product details
    product_page.verify_product_category(verify_category_all, verify_women_category, verify_women_product,
                                         verify_men_category, verify_men_product)



