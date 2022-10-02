class Event:
    title: str
    description: str
    event_date: str
    event_time: str
    type: str
    price: float

    def __init__(self, title: str, description: str, date: str, time: str, type: str, price: float):
        self.title = str(title)
        self.description = str(description)
        self.event_date = str(date)
        self.event_time = str(time)
        self.price = float(price)
        self.check_type(str(type))
        

    def check_type(self, type: str):
        types = ['FT', 'PU', 'PR']
        if type in types:
            self.type = type
            return True
        print(f"Invalid type. Valid types: {types}")
        self.type = 'FT'
        return False

    def render_obj(self):
        if self.type == 'FT':
            data = {
                    'Event': {
                        'title': self.title,
                        'description': self.description,
                        'event_date': self.event_date,
                        'event_time': self.event_time,
                        'type': self.type,
                    }
                }
        elif self.type == 'PU' or self.type == 'PR':
            data = {
                'Event': {
                    'title': self.title,
                    'description': self.description,
                    'event_date': self.event_date,
                    'event_time': self.event_time,
                    'type': self.type,
                    'price': self.price,
                }
            }
        else:
            return {}
        return data

class Guest:
    name: str
    phone: str

    def __init__(self, name: str, phone: str):
        self.name = str(name)
        self.check_phone(str(phone))

    def check_phone(self, phone: str):
        if len(phone) != 10 or not phone.isdigit():
            return print("Not a valid phone number")
        self.phone = phone

    def render_obj(self):
        return [self.name, self.phone]