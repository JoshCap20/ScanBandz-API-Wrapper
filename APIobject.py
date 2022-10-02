from AbstractAPI import Abstract_API
from ClassUtils import Event, Guest
from typing import Union
import requests

class API(Abstract_API):
    authenticated: bool = False

    def __init__(self):
        self.key_test()

    def key_test(self):
        """
        Verify API-KEY.
        """
        response = requests.get(self.endpoints['verify_endpoint'], headers=self.HEADERS)
        if self.check_valid_response(response):
            print("Valid API Key")
            self.authenticated = True
            return True
        return False
    
    def check_authenticated(self):
        """
        Test if key has been verified.
        """
        return self.authenticated

    def get_account(self):
        """
        Get account and billing cycle information.
        """
        response = requests.get(self.endpoints['acc_endpoint'], headers=self.HEADERS)
        return self.render_response(response)

    def get_events(self):
        """
        Get aggregate event information for all account related events.
        """
        response = requests.get(self.endpoints['events_endpoint'], headers=self.HEADERS)
        return self.render_response(response)

    def get_event(self, pk: Union[int, str]):
        """
        Get event details, given event primary key.
        """
        HEADERS = self.set_pk_header(pk)
        response = requests.get(self.endpoints['event_endpoint'], headers=HEADERS)
        return self.render_response(response)

    def add_guest(self, pk: Union[int, str], guest: Guest):
        """
        Add new guest to event, given event primary key and guest information.
        Guest obj constructor: Guest(name: str, phone: str)
        """
        HEADERS = self.set_pk_header(pk)
        data = self.set_guest_data(guest)
        response = requests.post(self.endpoints['event_endpoint'], headers=HEADERS, json=data)
        return self.render_response(response)

    def add_guests(self, pk: Union[int, str], guests: list[Guest]):
        """
        Add new guests to event, given event primary key and guest information.
        Example guests list: [Guest1, Guest2] where guests are Guest objects.
        """
        HEADERS = self.set_pk_header(pk)
        data = self.set_guests_data(guests)
        response = requests.post(self.endpoints['event_endpoint'], headers=HEADERS, json=data)
        return self.render_response(response)

    def new_event(self, event: Event):
        """
        Create a new event with an Event object.
        Event obj constructor: Event(title: str, description: str, date: str, time: str, type: str, price: float)
        """
        data = event.render_obj()
        response = requests.post(self.endpoints['events_endpoint'], headers=self.HEADERS, json=data)
        return self.render_response(response)

    def update_guest(self, pk, guests: list[Union[int, str]]):
        """
        Marks guests as attended. Pass a list of unique identifiers of either all PKs, all UUIDs, or telephone numbers.
        """
        HEADERS = self.set_pk_header(pk)
        response =requests.put(self.endpoints['event_endpoint'], headers=HEADERS, json={"Guests":guests})
        return self.render_response(response)

