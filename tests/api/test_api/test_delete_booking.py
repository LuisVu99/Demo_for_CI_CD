from tests.api.helpers.api_utils import APIHelpers

def test_delete_booking(client, create_body, token_body):
    #1. Create booking
    create_res = client.create_booking(data=create_body)
    booking_id = create_res.json()["bookingid"]

    # #2. Get Token
    token_res = client.get_token(data=token_body)
    token = token_res.json()["token"]
    headers = {
        "Cookie" : f"token={token}"
    }

    #3. Delete booking
    delete_res = client.delete_booking(booking_id, headers)
    APIHelpers.assert_status_code(delete_res, 201)
    
    #4. Verify booking deleted successfully
    check_res = client.get_a_booking(booking_id)
    assert check_res.status_code == 404
