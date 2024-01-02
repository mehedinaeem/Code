# admin.py

class FlightAdmin:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight_details):
        self.flights.append(flight_details)
        print("Flight added:", flight_details)

    def update_flight(self, flight_id, updated_details):
        for flight in self.flights:
            if flight['id'] == flight_id:
                flight.update(updated_details)
                print(f"Flight {flight_id} updated:", updated_details)

    def delete_flight(self, flight_id):
        self.flights = [flight for flight in self.flights if flight['id'] != flight_id]
        print(f"Flight {flight_id} deleted.")

    def get_all_flights(self):
        return self.flights
