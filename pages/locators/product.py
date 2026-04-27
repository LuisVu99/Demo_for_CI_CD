class ProductLocator:
    #Navigate to Product page
    PRODUCT_NAV = "//ul[@class='nav navbar-nav']//li[2]"
    ALL_PRODUCT_TITLE = "//h2[@class='title text-center']"
    PRODUCT_LIST = ".features_items .product-image-wrapper"

    #View product detail
    VIEW_PRODUCT_BUTTON= "(//ul[@class='nav nav-pills nav-justified']//a)[1]"
    PRODUCT_PICTURE = "//div[@class='view-product']//img"
    NEW_LABEL = "//div[@class='product-information']//img[@class='newarrival']"
    VIEW_PRODUCT_NAME = "//div[@class='product-information']//h2"
    CATEGORY = "(//div[@class='product-information']//p)[1]"
    PRICE = "//div[@class='product-information']//span//span"
    AVAILABILITY = "//div[@class='product-information']//p[2]"
    CONDITION = "//div[@class='product-information']//p[3]"
    BRAND_1 = "//div[@class='product-information']//p[4]"

    #Write a review
    WRITE_REVIEW = "//ul[@class='nav nav-tabs']"
    YOUR_NAME = "#name"
    EMAIL_ADDRESS = "#email"
    ADD_REVIEW = "#review"
    SUBMIT_BUTTON = "#button-review"
    VERIFY_SUCCESSFUL = "//div[@class='alert-success alert']//span"

    #Search product
    SEARCH_BOX = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCHED_PRODUCT = "//h2[@class='title text-center']"
    PRODUCT_NAME = "//div[@class='overlay-content']//p"

    #Category
    VERIFY_CATEGORY = "(//div[@class='left-sidebar']//h2)[1]"
    CLICK_WOMEN = "(//h4[@class='panel-title'])[1]//span"
    CLICK_DRESS = "//a[@href='/category_products/1']"
    VERIFY_CATEGORY_TITLE = "//ol[@class='breadcrumb']//li[2]"
    VERIFY_PRODUCT_TITLE = "//h2[@class='title text-center']"
    CLICK_MEN = "(//h4[@class='panel-title'])[2]//span"
    CLICK_TSHIRTS = "//a[@href='/category_products/3']"

    #Brand
    VERIFY_BRANDS = "(//div[@class='left-sidebar']//h2)[2]"
    CLICK_MADAME = "(//div[@class='brands-name']//a)[3]"
    VERIFY_BRAND_TITLE = "//ol[@class='breadcrumb']//li[2]"