class LoginLocator:
    #1. New user signup
    LOGIN_NAV = "//ul[@class='nav navbar-nav']//li[4]"
    SIGNUP_NAME = "//input[@placeholder='Name']"
    SIGNUP_EMAIL = "//input[@data-qa='signup-email']"
    SIGNUP_BUTTON= "//BUTTON[@data-qa='signup-button']"
    #2. Enter information
    ACCOUNT_INFORMATION = "(//h2[@class='title text-center'])[1]"
    TITLE = "//div[@class='radio-inline'][1]//label"
    PASS = "#password"
    DAY = "#days"
    MONTH = "#months"
    YEAR = "#years"
    ENABLE_SIGNUP = "//label[@for='newsletter']"
    ENABLE_RECEIVE = "//label[@for='optin']"

    ADDRESS_INFORMATION = "(//h2[@class='title text-center'])[2]"
    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"
    COMPANY = "#company"
    ADDRESS = "#address1"
    ADDRESS2 = "#address2"
    COUNTRY = "#country"
    STATE = "#state"
    CITY = "#city"
    ZIP = "#zipcode"
    PHONE = "#mobile_number"

    CREATE_BUTTON = "//button[@data-qa='create-account']"
    #3. Verify account created
    VERIFY_CREATED = "//h2[@class='title text-center']"
    CONTINUE_BUTTON = "//a[@data-qa='continue-button']"
    VERIFY_LOGIN = "//ul[@class='nav navbar-nav']//li[10]//a"

    #4. Delete account
    DELETE_ACCOUNT = "//a[contains(.,'Delete Account')]"

    #5. Login with account
    LOGIN_EMAIL = "//input[@data-qa='login-email']"
    LOGIN_PASS = "//input[@data-qa='login-password']"
    LOGIN_BUTTON = "//button[@data-qa='login-button']"
    INCORRECT_CREDENTIAL = "//form[@action='/login']//p"

    #5. Logout
    LOGOUT = "//a[contains(.,'Logout')]"
    VERIFY_LOGIN_PAGE = "//div[@class='login-form']//h2"
    SIGNUP_DUPLICATED_EMAIL = "//form[@action='/signup']//p"



