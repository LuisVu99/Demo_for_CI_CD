import pytest
from tests.api.booking_api import BookingAPI
from tests.api.helpers.api_utils import APIHelpers

def test_create_booking(client, create_body):
    response = client.create_booking(data=create_body)
    APIHelpers.assert_status_code(response, 200)
    booking = response.json()
    assert isinstance(booking["bookingid"], int)
    assert booking["booking"]["firstname"] == create_body["firstname"]
    assert booking["booking"]["lastname"] == create_body["lastname"]
    assert booking["booking"]["totalprice"] == create_body["totalprice"]
    assert booking["booking"]["depositpaid"] == create_body["depositpaid"]
    assert booking["booking"]["bookingdates"]["checkin"] == create_body["bookingdates"]["checkin"]
    assert booking["booking"]["bookingdates"]["checkout"] == create_body["bookingdates"]["checkout"]
    assert booking["booking"]["additionalneeds"] == create_body["additionalneeds"]
    
