import pytest
from tests.api.booking_api import BookingAPI
from tests.api.config import ConfigUrl, Credentials
from helpers.test_data import TestData

@pytest.fixture(scope="session")
def client():
    return BookingAPI(ConfigUrl.BASE_URL)

@pytest.fixture
def create_body():
    return {
        "firstname": TestData.random_first_name(),
        "lastname": TestData.random_last_name(),
        "totalprice": TestData.random_int(),
        "depositpaid": TestData.random_boolean(),
        "bookingdates": {
            "checkin": TestData.random_date_time(),
            "checkout": TestData.random_date_time(),
        },
        "additionalneeds": TestData.random_title()
    }

@pytest.fixture
def token_body():
    return {
        "username": Credentials.USER, 
        "password": Credentials.PASS
    }