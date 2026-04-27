from tests.api.base_api import BaseAPI
from tests.api.helpers.api_utils import APIHelpers

class BookingAPI(BaseAPI):
    def get_token(self, data):
        return self.post("/auth", data)
    
    def get_booking_all(self):
        return self.get("/booking")
    
    def create_booking(self, data):
        return self.post("/booking", data)
    
    def edit_booking(self, booking_id, data, headers = None, **kwargs):
        if not booking_id:
            raise ValueError("Booking ID not found in create response")
        return self.put(f"/booking/{booking_id}", data, headers=headers, **kwargs)
    
    def delete_booking(self, booking_id, headers):
        if not booking_id:
            raise ValueError("Booking ID not found in create response")
        return self.delete(f"/booking/{booking_id}", headers=headers)
    
    def get_a_booking(self, booking_id):
        if not booking_id:
            raise ValueError("Booking ID not found in create response")
        return self.get(f"/booking/{booking_id}")

