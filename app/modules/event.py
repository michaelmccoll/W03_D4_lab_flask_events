class Event():

    def __init__(self, date, name_event, number_of_guests, room_location, description,recurring=False):
        self.date= date
        self.name_event = name_event
        self.number_of_guests =number_of_guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring