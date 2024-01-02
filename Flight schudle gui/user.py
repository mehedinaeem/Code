# user.py

from PyQt5.QtWidgets import QWidget
class User:
    def search_flights(self, search_criteria, flights):
        results = []
        for flight in flights:
            if all(flight[key] == value for key, value in search_criteria.items()):
                results.append(flight)
        return results

    def subscribe_to_delay_notifications(self, flight_id, email):
        # Placeholder for subscribing to delay notifications
        print(f"Subscribed to delay notifications for Flight {flight_id} at {email}")
