from tests.api.booking_api import BookingAPI
from tests.api.helpers.api_utils import APIHelpers
from helpers.test_data import TestData


def test_edit_booking(client, create_body, token_body):
    #Create Booking
    create_response = client.create_booking(data=create_body)
    booking_id = create_response.json()["bookingid"]

    #Get Token
    token_res = client.get_token(data=token_body)
    token = token_res.json()["token"]
    headers = {
        "Cookie" : f"token={token}"
    }
    
    #Edit Booking
    edit_body = create_body.copy()
    edit_body["firstname"] = TestData.random_first_name()
    edit_body["lastname"] = TestData.random_last_name()
    edit_body["totalprice"] = TestData.random_int()
    edit_res = client.edit_booking(booking_id, data=edit_body, headers=headers)
    print(f"Request URL: {client}/booking/{booking_id}")
    # print(f"Status code: {response.status_code}")
    # print(f"Response body: {response.json()}")
    APIHelpers.assert_status_code(edit_res, 200)
    booking = edit_res.json()
    
    #assert booking["firstname"] == "Huong"
    APIHelpers.assert_json_value(booking, "firstname", edit_body["firstname"])
    APIHelpers.assert_json_value(booking, "lastname", edit_body["lastname"])
    APIHelpers.assert_json_value(booking, "totalprice", edit_body["totalprice"])
    APIHelpers.assert_json_value(booking, "depositpaid", create_body["depositpaid"])
    APIHelpers.assert_json_value(booking, "additionalneeds", create_body["additionalneeds"])
    assert booking["bookingdates"]["checkin"] == create_body["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == create_body["bookingdates"]["checkout"]
