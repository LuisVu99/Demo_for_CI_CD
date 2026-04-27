from pages.product_page import ProductPage

def test_search_product(page):
    product_page = ProductPage(page)

    #1.Prepare Data
    all_product_title = "All Products"
    product_name = "Sleeves Top"
    searched_product = "Searched Products"
    #2. Navigate to product
    product_page.navigate_to_product()
    #3. Verify all product
    product_page.verify_all_product(all_product_title)
    #4. Search product
    product_page.search_product(product_name, searched_product)