# ScanBandz API Python Wrapper

## Wrapper Public Methods
1. `key_test()` Tests if API-KEY is valid.
2. `get_account()` Get account and billing cycle information.
3. `get_events()` Get aggregate event information for all account related events.
4. `get_event(pk)` Get event details, given event primary key.
5. `add_guest(pk, guest)` Add new guest to event, given event primary key and guest information.
6. `add_guests(pk, guests)` Add new guests to event, given event primary key and guest information.
7. `new_event(event)` Create a new event with an Event object.
8. `update_guest(pk, guests)` Marks guests as attended. Pass a list of unique identifiers.

## Wrapper Attributes
1. `API_KEY` String

Configure API_KEY in settings.py.

[View Full API Documentation](https://scanbandz.com/api/v1/documentation).