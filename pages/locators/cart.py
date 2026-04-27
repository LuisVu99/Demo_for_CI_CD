class CartLocator:
    #Add two products to cart
    CARD_NAV = "//ul[@class='nav navbar-nav']//li[3]"
    PRODUCT_NAV = "//ul[@class='nav navbar-nav']//li[2]"
    ADD_FIRST_PRODUCT = "(//a[@class='btn btn-default add-to-cart'])[1]"
    ADD_SECOND_PRODUCT = "(//a[@class='btn btn-default add-to-cart'])[5]"
    CONTINUE_SHOPPING = "//button[.='Continue Shopping']"

    #View product 1 in cart
    VIEW_CART = "//p[@class='text-center']//a//u"
    ITEM_1_PICTURE = "(//div[@id='cart_info']//img)[1]"
    ITEM_1_NAME = "(//td[@class='cart_description']//a)[1]"
    ITEM_1_PRICE = "(//td[@class='cart_price']//p)[1]"
    ITEM_1_QUANTITY = "(//td[@class='cart_quantity']//button)[1]"
    ITEM_1_TOTAL = "(//p[@class='cart_total_price'])[1]"

    #View product 2 in cart
    ITEM_2_PICTURE = "(//div[@id='cart_info']//img)[2]"
    ITEM_2_NAME = "(//td[@class='cart_description']//a)[2]"
    ITEM_2_PRICE = "(//td[@class='cart_price']//p)[2]"
    ITEM_2_QUANTITY = "(//td[@class='cart_quantity']//button)[2]"
    ITEM_2_TOTAL = "(//p[@class='cart_total_price'])[2]"

    # Increase quantity of product
    QUANTITY_ITEM = "#quantity"
    ADD_TO_CART = "//button[@class='btn btn-default cart']"

    # Delete product
    DELETE_ITEM = "//a[@class='cart_quantity_delete']"
    EMPTY_CARD = "//span[@id='empty_cart']"

    #Checkout
    PROCEED_TO_CHECKOUT = "//a[@class='btn btn-default check_out']"
    CHECKOUT_BUTTON = ""
    ADDRESS_DETAILS = "//h2[.='Address Details']"
    #Delivery address
    DELIVERY_ADDRESS = "//ul[@class='address item box']//li[1]"
    DELIVERY_NAME = "//ul[@class='address item box']//li[2]"
    DELIVERY_COMPANY = "//ul[@class='address item box']//li[3]"
    DELIVERY_ADDRESS_1 = "//ul[@class='address item box']//li[4]"
    DELIVERY_ADDRESS_2 = "//ul[@class='address item box']//li[5]"
    DELIVERY_ADDRESS_FULL = "//ul[@class='address item box']//li[6]"
    DELIVERY_ADDRESS_COUNTRY = "//ul[@class='address item box']//li[7]"
    DELIVERY_PHONE = "//ul[@class='address item box']//li[8]"
    #Billing address
    BILLING_ADDRESS = "//ul[@class='address alternate_item box']//li[1]"
    BILLING_NAME = "//ul[@class='address alternate_item box']//li[2]"
    BILLING_COMPANY = "//ul[@class='address alternate_item box']//li[3]"
    BILLING_ADDRESS_1 = "//ul[@class='address alternate_item box']//li[4]"
    BILLING_ADDRESS_2 = "//ul[@class='address alternate_item box']//li[5]"
    BILLING_ADDRESS_FULL = "//ul[@class='address alternate_item box']//li[6]"
    BILLING_ADDRESS_COUNTRY = "//ul[@class='address alternate_item box']//li[7]"
    BILLING_PHONE = "//ul[@class='address alternate_item box']//li[8]"
    #Review Your Order
    REVIEW_ORDER = "//h2[.='Review Your Order']"
    CHECKOUT_PICTURE_1 = "(//td[@class='cart_product']//img)[1]"
    CHECKOUT_PICTURE_2 = "(//td[@class='cart_product']//img)[2]"
    TOTAL_AMOUNT_TEXT = "//table[@class='table table-condensed']//b"
    TOTAL_PRICE = "(//p[@class='cart_total_price'])[3]"
    COMMENT_DESCRIPTION = "//div[@id='ordermsg']//label"
    COMMENT_INPUT = "//div[@id='ordermsg']//textarea"
    PLACE_ORDER = "//a[.='Place Order']"

    #Add recommended item
    ADD_FIRST_RECOMMENDED_PRODUCT = "(//div[@id='recommended-item-carousel']//a)[1]"
    ADD_SECOND_RECOMMENDED_PRODUCT = "(//div[@id='recommended-item-carousel']//a)[3]"

    #Payment
    PAYMENT_TITLE = "//div[@class='step-one']//h2"
    NAME_CARD = "//input[@data-qa='name-on-card']"
    CARD_NUMBER = "//input[@data-qa='card-number']"
    CVC = "//input[@data-qa='cvc']"
    EXPIRATION_MONTH = "//input[@data-qa='expiry-month']"
    EXPIRATION_YEAR = "//input[@data-qa='expiry-year']"
    CONFIRM_BUTTON = "#submit"
    SUCCESSFULLY_ORDER_INPAYMENT = "text=Your order has been placed successfully!"

    #Order successfully
    ORDER_PLACED = "//h2[@class='title text-center']"
    SUCCESSFULLY_ORDER_MESSAGE = "(//div[@class='row']//p)[1]"
    DOWNLOAD_INVOICE = "//a[.='Download Invoice']"
    CONTINUE_BUTTON = "//a[@data-qa='continue-button']"