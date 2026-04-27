from pages.product_page import ProductPage

def test_verify_brand(page):
    product_page = ProductPage(page)

    #1.Prepare Data
    all_product_title = "All Products"
    verify_brand_all = "Brands"
    verify_brand_title = "Madame"
    verify_madame_product = "Brand - Madame Products"
    #2. Navigate to product
    product_page.navigate_to_product()
    #3. Verify all product
    product_page.verify_all_product(all_product_title)
    #4. View product details
    product_page.verify_product_brand(verify_brand_all, verify_brand_title, verify_madame_product)



