class ContactUsLocator:
    #1. Navigate to Contact Us
    HOME_PAGE = "//ul[@class='nav navbar-nav']//li[1]//a[@style='color: orange;']"
    CONTACTUS_PAGE = "//a[.=' Contact us']"
    #2. Fill into feedback form
    GET_IN_TOUCH = "//div[@class='contact-form']//h2"
    NAME = "//input[@data-qa='name']"
    EMAIL = "//input[@data-qa='email']"
    SUBJECT = "//input[@data-qa='subject']"
    YOUR_MESSAGE = "#message"
    UPLOAD_FILE = "//input[@name='upload_file']"
    SUBMIT_BUTTON = 'input[name="submit"]'
    VERIFY_SUBMIT_SUCCESSFULLY = "//div[@class='status alert alert-success']"
    HOME_BUTTON = "//a[@class='btn btn-success']"


