from tests.api.booking_api import BookingAPI
from tests.api.helpers.api_utils import APIHelpers

def test_get_all_bookings(client):
    response = client.get_booking_all()
    APIHelpers.assert_status_code(response, 200)
    APIHelpers.assert_json_key(response.json(), ["bookingid"])
    for booking in response.json():
        assert "bookingid" in booking
        assert isinstance(booking["bookingid"], int)

    
