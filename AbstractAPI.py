
from settings import *


class Abstract_API:
    API_KEY: str = API_KEY
    HEADERS: dict = {
            'Authorization': API_KEY,
        }
    endpoints: str = {
        'events_endpoint': ENDPOINT + EVENTS_ENDPOINT,
        'event_endpoint': ENDPOINT + EVENT_ENDPOINT,
        'acc_endpoint': ENDPOINT + ACC_ENDPOINT,
        'verify_endpoint': ENDPOINT + VERIFY_ENDPOINT,
    }

    def check_valid_response(self, response):
        success_codes: list[int] = [200, 201, 202, 203, 204]
        if response.status_code in success_codes:
            return True
        elif response.status_code == 401:
            print("Response - Unauthorized.")
        elif response.status_code == 404:
            print("Response - Not found.")
        elif response.status_code == 400:
            print("Response - Invalid request")
        elif response.status_code == 429:
            print("Response - Request threshold error")
        elif response.status_code == 405:
            print("Response - Method Not Allowed")
        else:
            print(response.status_code)
        return False

    def merge_dict(self, newdict):
        return(newdict.update(self.HEADERS))
    
    def render_response(self, response):
        self.check_valid_response(response)
        return response.json()

    def set_pk_header(self, pk):
        pk = str(pk)
        HEADERS = {
            'Event': pk,
        }
        self.merge_dict(HEADERS)
        return HEADERS

    def set_guest_data(self, guest):
        data = {
            'Guests': [guest.render_obj()]
        }
        return data

    def set_guests_data(self, guests):
        data = {
            'Guests': [guest.render_obj() for guest in guests]
        }
        return data

    def key_test(self):
        raise NotImplementedError("The method is not implemented.")
    
    def get_account(self):
        raise NotImplementedError("The method is not implemented.")

    def get_events(self):
        raise NotImplementedError("The method is not implemented.")

    def get_event(self, **kwargs):
        raise NotImplementedError("The method is not implemented.")

    def add_guest(self, **kwargs):
        raise NotImplementedError("The method is not implemented.")
    
    def add_guests(self, **kwargs):
        raise NotImplementedError("The method is not implemented.")

    def new_event(self, **kwargs):
        raise NotImplementedError("The method is not implemented.")

    def update_guest(self, **kwargs):
        raise NotImplementedError("The method is not implemented.")