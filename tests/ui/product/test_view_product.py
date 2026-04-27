from pages.product_page import ProductPage

def test_view_product(page):
    product_page = ProductPage(page)

    #1.Prepare Data
    all_product_title = "All Products"
    attribute_picture = "src"
    attribute_picture_value = "/get_product_picture/1"
    attribute_new_label = "src"
    attribute_new_label_value = "/static/images/product-details/new.jpg"
    product_name = "Blue Top"
    category = "Category: Women > Tops"
    price = "Rs. 500"
    availability = "Availability: In Stock"
    condition = "Condition: New"
    brand = "Brand: Polo"
    #2. Navigate to product
    product_page.navigate_to_product()
    #3. Verify all product
    product_page.verify_all_product(all_product_title)
    #2. View product details
    product_page.view_product_detail(attribute_picture, attribute_picture_value, attribute_new_label, attribute_new_label_value,
                                     product_name, category, price, availability, condition, brand)



