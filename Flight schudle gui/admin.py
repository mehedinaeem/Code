# admin.py

from PyQt5.QtWidgets import QWidget

class FlightAdmin:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight_details):
        self.flights.append(flight_details)

    def update_flight(self, flight_id, updated_details):
        for flight in self.flights:
            if flight['id'] == flight_id:
                flight.update(updated_details)

    def delete_flight(self, flight_id):
        self.flights = [flight for flight in self.flights if flight['id'] != flight_id]

    def get_all_flights(self):
        return self.flights
